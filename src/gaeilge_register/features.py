"""Surface feature extraction for Irish text.

Design rules:
  * rule-based and inspectable, no model, no network access;
  * every flag is a candidate, reported with the rule that produced it;
  * counts are per text, never per author. Do not aggregate by person.
"""
from __future__ import annotations

import re
import unicodedata
from dataclasses import asdict, dataclass, field

from . import lexicons as lx

TOKEN_RE = re.compile(r"[@#]?[A-Za-zÁÉÍÓÚáéíóú]+(?:[-'’][A-Za-zÁÉÍÓÚáéíóú]+)*|\d+|\S")
WORD_RE = re.compile(r"^[A-Za-zÁÉÍÓÚáéíóú]+(?:[-'’][A-Za-zÁÉÍÓÚáéíóú]+)*$")
ELONGATION_RE = re.compile(r"(.)\1{2,}")
FADA = set("áéíóúÁÉÍÓÚ")

LENITABLE = set("bcdfgmpst")
# s does not lenite before these consonants (sc, sf, sm, sp, st, sv).
S_BLOCKERS = set("cfmptv")
ECLIPSIS = {"b": "mb", "c": "gc", "d": "nd", "f": "bhf", "g": "ng", "p": "bp", "t": "dt"}
ECLIPSED_PREFIXES = tuple(ECLIPSIS.values())

LENITION_TRIGGERS = frozenset({"mo", "do"})
ECLIPSIS_TRIGGERS = frozenset({"ár", "bhur", "i"})


def tokenise(text: str) -> list[str]:
    return TOKEN_RE.findall(text)


def strip_fada(s: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn"
    )


def is_word(tok: str) -> bool:
    return bool(WORD_RE.match(tok))


def _lenition_expected(word: str) -> bool:
    """True if `word` begins with a consonant that lenition would mark."""
    w = word.lower()
    if len(w) < 2 or w[0] not in LENITABLE:
        return False
    if w[0] == "s" and w[1] in S_BLOCKERS:
        return False
    return True


def _is_lenited(word: str) -> bool:
    return len(word) > 1 and word[1].lower() == "h"


def _eclipsis_expected(word: str) -> bool:
    w = word.lower()
    return bool(w) and w[0] in ECLIPSIS and not w.startswith(ECLIPSED_PREFIXES)


def lenition_candidates(tokens: list[str], skip_capitalised: bool = True):
    """Yield (index, trigger, word) where lenition after mo/do is expected
    under the Caighdeán Oifigiúil but is not written.

    `do` is ambiguous (possessive, preposition, verbal particle) and all three
    lenite, which is why it is usable without tagging. Capitalised words are
    skipped by default because names and English insertions are often left
    unmutated in every variety.
    """
    for i in range(len(tokens) - 1):
        if tokens[i].lower() not in LENITION_TRIGGERS:
            continue
        nxt = tokens[i + 1]
        if not is_word(nxt) or (skip_capitalised and nxt[0].isupper()):
            continue
        if _lenition_expected(nxt) and not _is_lenited(nxt):
            yield i + 1, tokens[i].lower(), nxt


def eclipsis_candidates(tokens: list[str]):
    """Yield (index, trigger, word) where eclipsis after ár/bhur/i is expected
    but is not written. Lower-case `i` only, to avoid the English pronoun."""
    for i in range(len(tokens) - 1):
        trig = tokens[i]
        if trig.lower() not in ECLIPSIS_TRIGGERS or trig == "I":
            continue
        nxt = tokens[i + 1]
        if is_word(nxt) and _eclipsis_expected(nxt):
            yield i + 1, trig.lower(), nxt


def mutation_context_counts(tokens: list[str]) -> dict:
    """Counts with denominators, for raw text without part-of-speech tags.

    Lenition contexts are mo/do before a lower-case word with a lenitable
    initial. Eclipsis contexts are ár/bhur/lower-case i before a word with an
    eclipsable initial. A lenited word in an eclipsis context is not counted
    as unmarked, since some dialects lenite there.
    """
    c = {"len_contexts": 0, "len_unmarked": 0, "ecl_contexts": 0, "ecl_unmarked": 0}
    for i in range(len(tokens) - 1):
        trig, nxt = tokens[i], tokens[i + 1]
        if not is_word(nxt) or len(nxt) < 2:
            continue
        low = trig.lower()
        if low in LENITION_TRIGGERS and not nxt[0].isupper() and (
            _lenition_expected(nxt) or (_is_lenited(nxt) and nxt[0].lower() in LENITABLE)
        ):
            c["len_contexts"] += 1
            c["len_unmarked"] += not _is_lenited(nxt)
        if low in ECLIPSIS_TRIGGERS and trig != "I":
            w = nxt.lower()
            if w.startswith(ECLIPSED_PREFIXES):
                c["ecl_contexts"] += 1
            elif w[0] in ECLIPSIS:
                c["ecl_contexts"] += 1
                c["ecl_unmarked"] += not _is_lenited(nxt)
    return c


def copula_candidates(tokens: list[str]):
    """Yield indices of `tá/bhí/níl + pronoun + class noun`, the pattern where
    the standard language uses the copula (Is múinteoir é). Lexicon-bound."""
    low = [t.lower() for t in tokens]
    for i in range(len(low) - 2):
        if (
            low[i] in lx.BI_FORMS
            and low[i + 1] in lx.SUBJECT_PRONOUNS
            and low[i + 2] in lx.CLASS_NOUNS
        ):
            yield i


@dataclass
class FeatureReport:
    n_tokens: int = 0
    n_words: int = 0
    words_with_fada: int = 0
    missing_fada: list = field(default_factory=list)
    english_function_words: int = 0
    discourse_markers: dict = field(default_factory=dict)
    abbreviations: list = field(default_factory=list)
    intensifier_an_mixed: list = field(default_factory=list)
    elongations: list = field(default_factory=list)
    lenition_candidates: list = field(default_factory=list)
    eclipsis_candidates: list = field(default_factory=list)
    copula_candidates: int = 0
    mentions_hashtags: int = 0

    def per_1000_words(self) -> dict:
        d = max(self.n_words, 1)
        rate = lambda n: round(1000 * n / d, 2)  # noqa: E731
        return {
            "words": self.n_words,
            "fada_bearing_words": rate(self.words_with_fada),
            "missing_fada_candidates": rate(len(self.missing_fada)),
            "english_function_words": rate(self.english_function_words),
            "discourse_markers": rate(sum(self.discourse_markers.values())),
            "abbreviations": rate(len(self.abbreviations)),
            "elongations": rate(len(self.elongations)),
            "lenition_candidates": rate(len(self.lenition_candidates)),
            "eclipsis_candidates": rate(len(self.eclipsis_candidates)),
            "copula_candidates": rate(self.copula_candidates),
        }

    def to_dict(self) -> dict:
        d = asdict(self)
        d["per_1000_words"] = self.per_1000_words()
        return d


def analyse(text: str | list[str]) -> FeatureReport:
    """Analyse a string, or a pre-tokenised list of forms."""
    tokens = tokenise(text) if isinstance(text, str) else list(text)
    r = FeatureReport(n_tokens=len(tokens))
    for tok in tokens:
        if tok[:1] in "@#" and len(tok) > 1:
            r.mentions_hashtags += 1
            continue
        if not is_word(tok):
            continue
        r.n_words += 1
        low = tok.lower()
        if FADA & set(tok):
            r.words_with_fada += 1
        if low in lx.MISSING_FADA:
            r.missing_fada.append((tok, lx.MISSING_FADA[low]))
        if low in lx.ENGLISH_FUNCTION_WORDS:
            r.english_function_words += 1
        if low in lx.DISCOURSE_MARKERS:
            r.discourse_markers[low] = r.discourse_markers.get(low, 0) + 1
        if low in lx.ABBREVIATIONS:
            r.abbreviations.append(tok)
        if low.startswith("an-") and strip_fada(low[3:]) in lx.ENGLISH_FUNCTION_WORDS | {
            "time", "talent", "cool", "fun", "happy", "excited", "class"
        }:
            r.intensifier_an_mixed.append(tok)
        if ELONGATION_RE.search(low):
            r.elongations.append(tok)
    r.lenition_candidates = [(t, w) for _, t, w in lenition_candidates(tokens)]
    r.eclipsis_candidates = [(t, w) for _, t, w in eclipsis_candidates(tokens)]
    r.copula_candidates = sum(1 for _ in copula_candidates(tokens))
    return r
