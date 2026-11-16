#!/usr/bin/env python3
"""Compare edited Irish (UD Irish-IDT) with Irish tweets (UD Irish-TwittIrish).

Outputs aggregate counts only. No tweet text is written to disk or stdout.

Usage (run with -I because the treebanks are downloaded data):
    python3 -I scripts/compare_treebanks.py \
        --idt external/UD_Irish-IDT --twittirish external/UD_Irish-TwittIrish \
        --out results
"""
import argparse
import collections
import glob
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))

from gaeilge_register import lexicons as lx  # noqa: E402
from gaeilge_register.conllu import read_sentences  # noqa: E402
from gaeilge_register.features import (  # noqa: E402
    FADA, _eclipsis_expected, _is_lenited, _lenition_expected, is_word, strip_fada,
)

NON_WORD_UPOS = {"PUNCT", "SYM"}


def pct(n, d):
    return round(100 * n / d, 2) if d else None


def per1000(n, d):
    return round(1000 * n / d, 2) if d else None


def wilson(k, n, z=1.96):
    """95% Wilson score interval for a proportion, in percent."""
    if not n:
        return None
    p = k / n
    d = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / d
    half = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / d
    return [round(100 * (centre - half), 1), round(100 * (centre + half), 1)]


def load(folder):
    sents = []
    for f in sorted(glob.glob(os.path.join(folder, "*.conllu"))):
        sents.extend(read_sentences(f))
    if not sents:
        sys.exit(f"no .conllu files in {folder}")
    return sents


def classify_correction(form, correct):
    """Bucket a (written form, annotated CorrectForm) pair."""
    if form == correct:
        return "identical"
    if form.lower() == correct.lower():
        return "case_only"
    if strip_fada(form.lower()) == strip_fada(correct.lower()):
        return "diacritic_only"
    f, c = strip_fada(form.lower()), strip_fada(correct.lower())
    if c.replace("h", "") == f.replace("h", "") or c.lstrip("mgnbd") == f.lstrip("mgnbd"):
        return "mutation_or_h"
    if f.replace(" ", "").replace("-", "") == c.replace(" ", "").replace("-", ""):
        return "spacing_or_hyphen"
    return "other_spelling"


def surface(sents):
    """Counts that need only FORM and UPOS, so they apply to both treebanks."""
    c = collections.Counter()
    upos = collections.Counter()
    for s in sents:
        c["sentences"] += 1
        c["tokens"] += len(s)
        for i, t in enumerate(s):
            upos[t.upos] += 1
            if t.upos in NON_WORD_UPOS or not is_word(t.form):
                continue
            c["words"] += 1
            low = t.form.lower()
            if FADA & set(t.form):
                c["fada_words"] += 1
            if low in lx.DISCOURSE_MARKERS:
                c["discourse_markers"] += 1
            if low in lx.ENGLISH_FUNCTION_WORDS:
                c["english_function_words"] += 1
            if low in lx.MISSING_FADA:
                c["missing_fada_candidates"] += 1
            if low in lx.ABBREVIATIONS:
                c["abbreviations"] += 1
            # mutation contexts: trigger followed by a common noun
            if i + 1 < len(s) and s[i + 1].upos == "NOUN" and is_word(s[i + 1].form):
                nxt = s[i + 1]
                if low in ("mo", "do") and _lenition_expected(nxt.form):
                    c["len_contexts"] += 1
                    if not _is_lenited(nxt.form):
                        c["len_unmarked"] += 1
                        if nxt.misc.get("Lang") == "en" or nxt.feats.get("Foreign") == "Yes":
                            c["len_unmarked_foreign"] += 1
                    if "Form" in nxt.feats:
                        c["len_gold_available"] += 1
                        if "Len" in nxt.feats["Form"]:
                            c["len_gold_len"] += 1
                if (low in ("ár", "bhur") or t.form == "i") and nxt.form[0].lower() in "bcdfgpt":
                    c["ecl_contexts"] += 1
                    if _eclipsis_expected(nxt.form):
                        c["ecl_unmarked"] += 1
                        if nxt.misc.get("Lang") == "en" or nxt.feats.get("Foreign") == "Yes":
                            c["ecl_unmarked_foreign"] += 1
    w = c["words"]
    return {
        "sentences": c["sentences"],
        "tokens": c["tokens"],
        "words": w,
        "mean_tokens_per_sentence": round(c["tokens"] / c["sentences"], 2),
        "upos_pct": {k: pct(v, c["tokens"]) for k, v in upos.most_common()},
        "fada_bearing_words_pct": pct(c["fada_words"], w),
        "per_1000_words": {
            "discourse_markers": per1000(c["discourse_markers"], w),
            "english_function_words": per1000(c["english_function_words"], w),
            "missing_fada_candidates": per1000(c["missing_fada_candidates"], w),
            "abbreviations": per1000(c["abbreviations"], w),
        },
        "mutation_after_trigger": {
            "lenition_contexts_mo_do_NOUN": c["len_contexts"],
            "lenition_unmarked": c["len_unmarked"],
            "lenition_unmarked_pct": pct(c["len_unmarked"], c["len_contexts"]),
            "lenition_unmarked_ci95": wilson(c["len_unmarked"], c["len_contexts"]),
            "lenition_unmarked_foreign_noun": c["len_unmarked_foreign"],
            "gold_Form_available": c["len_gold_available"],
            "gold_Form_Len_pct": pct(c["len_gold_len"], c["len_gold_available"]),
            "eclipsis_contexts_ar_bhur_i_NOUN": c["ecl_contexts"],
            "eclipsis_unmarked": c["ecl_unmarked"],
            "eclipsis_unmarked_pct": pct(c["ecl_unmarked"], c["ecl_contexts"]),
            "eclipsis_unmarked_ci95": wilson(c["ecl_unmarked"], c["ecl_contexts"]),
            "eclipsis_unmarked_foreign_noun": c["ecl_unmarked_foreign"],
        },
    }


def idt_gold(sents):
    c = collections.Counter()
    dialect = collections.Counter()
    for s in sents:
        for t in s:
            if t.upos in NON_WORD_UPOS:
                continue
            c["words"] += 1
            for k in ("Foreign", "Typo", "Abbr"):
                if t.feats.get(k) == "Yes":
                    c[k] += 1
            if "Dialect" in t.feats:
                dialect[t.feats["Dialect"]] += 1
    w = c["words"]
    return {
        "words_excl_punct_sym": w,
        "Foreign_per_1000": per1000(c["Foreign"], w),
        "Typo_per_1000": per1000(c["Typo"], w),
        "Abbr_per_1000": per1000(c["Abbr"], w),
        "Dialect_tagged_tokens": dict(dialect),
        "Dialect_per_1000": per1000(sum(dialect.values()), w),
    }


def twitt_gold(sents):
    c = collections.Counter()
    lang = collections.Counter()
    cstype = collections.Counter()
    corr = collections.Counter()
    en_upos = collections.Counter()
    for s in sents:
        langs = set()
        for t in s:
            lg = t.misc.get("Lang", t.misc.get("LLang"))
            if lg:
                lg = lg.lower()
                lang[lg] += 1
                langs.add(lg)
                if lg == "en":
                    en_upos[t.upos] += 1
            if "CSType" in t.misc:
                cstype[t.misc["CSType"]] += 1
            if t.upos in NON_WORD_UPOS:
                continue
            c["words"] += 1
            if "CorrectForm" in t.misc:
                c["CorrectForm"] += 1
                corr[classify_correction(t.form, t.misc["CorrectForm"])] += 1
            if "FullForm" in t.misc:
                c["FullForm"] += 1
        c["tweets"] += 1
        if "en" in langs:
            c["tweets_with_en"] += 1
        if "en" in langs and "ga" in langs:
            c["tweets_ga_and_en"] += 1
        if langs - {"ga"}:
            c["tweets_with_non_ga"] += 1
    w = c["words"]
    tagged = sum(lang.values())
    return {
        "words_excl_punct_sym": w,
        "lang_tagged_tokens": tagged,
        "lang_pct_of_tagged": {k: pct(v, tagged) for k, v in lang.most_common()},
        "tweets": c["tweets"],
        "tweets_with_english_token_pct": pct(c["tweets_with_en"], c["tweets"]),
        "tweets_with_irish_and_english_pct": pct(c["tweets_ga_and_en"], c["tweets"]),
        "tweets_with_any_non_irish_token_pct": pct(c["tweets_with_non_ga"], c["tweets"]),
        "CSType_counts": dict(cstype.most_common()),
        "english_token_upos_pct": {k: pct(v, lang["en"]) for k, v in en_upos.most_common(8)},
        "CorrectForm_tokens": c["CorrectForm"],
        "CorrectForm_per_1000": per1000(c["CorrectForm"], w),
        "CorrectForm_type_pct": {k: pct(v, c["CorrectForm"]) for k, v in corr.most_common()},
        "FullForm_abbreviation_tokens": c["FullForm"],
        "FullForm_per_1000": per1000(c["FullForm"], w),
    }


def to_markdown(res):
    i, t = res["surface"]["IDT"], res["surface"]["TwittIrish"]
    rows = [
        ("Sentences / tweets", i["sentences"], t["sentences"]),
        ("Tokens", i["tokens"], t["tokens"]),
        ("Word tokens (alphabetic, not PUNCT/SYM)", i["words"], t["words"]),
        ("Mean tokens per sentence / tweet", i["mean_tokens_per_sentence"], t["mean_tokens_per_sentence"]),
        ("Words carrying a síneadh fada (%)", i["fada_bearing_words_pct"], t["fada_bearing_words_pct"]),
        ("PROPN share of tokens (%)", i["upos_pct"].get("PROPN"), t["upos_pct"].get("PROPN")),
        ("SYM share of tokens (%)", i["upos_pct"].get("SYM"), t["upos_pct"].get("SYM")),
        ("INTJ share of tokens (%)", i["upos_pct"].get("INTJ"), t["upos_pct"].get("INTJ")),
        ("VERB share of tokens (%)", i["upos_pct"].get("VERB"), t["upos_pct"].get("VERB")),
    ]
    for k, label in [
        ("discourse_markers", "English discourse markers (8-item list) per 1,000 words"),
        ("english_function_words", "English function words (list) per 1,000 words"),
        ("missing_fada_candidates", "Missing-fada candidates (30-item list) per 1,000 words"),
        ("abbreviations", "Listed initialisms (GRMA etc.) per 1,000 words"),
    ]:
        rows.append((label, i["per_1000_words"][k], t["per_1000_words"][k]))
    mi, mt = i["mutation_after_trigger"], t["mutation_after_trigger"]
    rows += [
        ("mo/do + lenitable common noun: contexts", mi["lenition_contexts_mo_do_NOUN"], mt["lenition_contexts_mo_do_NOUN"]),
        ("... written without lenition (%)", mi["lenition_unmarked_pct"], mt["lenition_unmarked_pct"]),
        ("... 95% Wilson interval", mi["lenition_unmarked_ci95"], mt["lenition_unmarked_ci95"]),
        ("... of which noun tagged English/foreign (n)", mi["lenition_unmarked_foreign_noun"], mt["lenition_unmarked_foreign_noun"]),
        ("ár/bhur/i + eclipsable common noun: contexts", mi["eclipsis_contexts_ar_bhur_i_NOUN"], mt["eclipsis_contexts_ar_bhur_i_NOUN"]),
        ("... written without eclipsis (%)", mi["eclipsis_unmarked_pct"], mt["eclipsis_unmarked_pct"]),
        ("... 95% Wilson interval", mi["eclipsis_unmarked_ci95"], mt["eclipsis_unmarked_ci95"]),
        ("... of which noun tagged English/foreign (n)", mi["eclipsis_unmarked_foreign_noun"], mt["eclipsis_unmarked_foreign_noun"]),
    ]
    out = ["# Treebank comparison: edited Irish vs Irish tweets", "",
           "Generated by `scripts/compare_treebanks.py`. Aggregate counts only.", "",
           "## Surface measures (same code on both treebanks)", "",
           "| Measure | UD Irish-IDT | UD Irish-TwittIrish |", "|---|---:|---:|"]
    out += [f"| {a} | {b} | {c} |" for a, b, c in rows]
    g = res["gold"]["TwittIrish"]
    out += ["", "## TwittIrish gold annotation (MISC column)", "",
            f"- Tweets: {g['tweets']}; language-tagged tokens: {g['lang_tagged_tokens']}",
            f"- Language of tagged tokens (%): {g['lang_pct_of_tagged']}",
            f"- Tweets containing at least one English-tagged token: {g['tweets_with_english_token_pct']}%",
            f"- Tweets containing both Irish- and English-tagged tokens: {g['tweets_with_irish_and_english_pct']}%",
            f"- Tweets containing any non-Irish-tagged token: {g['tweets_with_any_non_irish_token_pct']}%",
            f"- UPOS of English-tagged tokens (%): {g['english_token_upos_pct']}",
            f"- CSType values (raw labels): {g['CSType_counts']}",
            f"- Tokens with a `CorrectForm` annotation: {g['CorrectForm_tokens']} ({g['CorrectForm_per_1000']} per 1,000 words)",
            f"- `CorrectForm` difference type (%): {g['CorrectForm_type_pct']}",
            f"- Tokens with a `FullForm` (abbreviation expansion): {g['FullForm_abbreviation_tokens']} ({g['FullForm_per_1000']} per 1,000 words)"]
    g = res["gold"]["IDT"]
    out += ["", "## IDT gold annotation (FEATS column)", "",
            f"- Foreign=Yes: {g['Foreign_per_1000']} per 1,000 words",
            f"- Typo=Yes: {g['Typo_per_1000']} per 1,000 words",
            f"- Abbr=Yes: {g['Abbr_per_1000']} per 1,000 words",
            f"- Dialect-tagged tokens: {g['Dialect_tagged_tokens']} ({g['Dialect_per_1000']} per 1,000 words)",
            f"- Rule check: of mo/do + lenitable common noun contexts with a gold `Form` value, "
            f"{mi['gold_Form_Len_pct']}% are gold `Form=Len` (n={mi['gold_Form_available']})", ""]
    return "\n".join(out)


def main():  # noqa: C901
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--idt", required=True)
    ap.add_argument("--twittirish", required=True)
    ap.add_argument("--out", default="results")
    a = ap.parse_args()
    idt, tw = load(a.idt), load(a.twittirish)
    res = {
        "surface": {"IDT": surface(idt), "TwittIrish": surface(tw)},
        "gold": {"IDT": idt_gold(idt), "TwittIrish": twitt_gold(tw)},
    }
    os.makedirs(a.out, exist_ok=True)
    with open(os.path.join(a.out, "treebank_comparison.json"), "w", encoding="utf-8") as fh:
        json.dump(res, fh, ensure_ascii=False, indent=2)
    md = to_markdown(res)
    with open(os.path.join(a.out, "treebank_comparison.md"), "w", encoding="utf-8") as fh:
        fh.write(md)
    print(md)


if __name__ == "__main__":
    main()
