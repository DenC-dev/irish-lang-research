#!/usr/bin/env python3
"""Compare the two sub-corpora inside UD Irish-TwittIrish.

LTC tweets were posted 2009-2014 and NTC tweets 2010-2019 (treebank README).
The sent_id prefix records which sub-corpus a tweet came from. The periods
overlap and the two were sampled differently, so this is a coarse
earlier-versus-later contrast, not a time series.

Aggregate counts only. Usage:
    python3 -I scripts/compare_cohorts.py --twittirish external/UD_Irish-TwittIrish --out results
"""
import argparse
import collections
import glob
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))

from compare_treebanks import classify_correction, wilson  # noqa: E402
from gaeilge_register import lexicons as lx  # noqa: E402
from gaeilge_register.conllu import _kv, Token  # noqa: E402
from gaeilge_register.features import FADA, is_word  # noqa: E402


def read_with_ids(path):
    sid, sent = None, []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if line.startswith("# sent_id"):
                sid = line.split("=", 1)[1].strip()
            elif not line:
                if sent:
                    yield sid, sent
                sid, sent = None, []
            elif not line.startswith("#"):
                c = line.split("\t")
                if len(c) == 10 and c[0].isdigit():
                    sent.append(Token(c[1], c[2], c[3], _kv(c[5]), _kv(c[9])))
    if sent:
        yield sid, sent


def two_prop_z(k1, n1, k2, n2):
    """Two-sided p-value for a difference in proportions (normal approx.)."""
    if not n1 or not n2:
        return None
    p = (k1 + k2) / (n1 + n2)
    se = math.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
    if se == 0:
        return None
    z = (k1 / n1 - k2 / n2) / se
    return round(math.erfc(abs(z) / math.sqrt(2)), 4)


def tally(sents):
    c = collections.Counter()
    for s in sents:
        c["tweets"] += 1
        c["tokens"] += len(s)
        langs = {(t.misc.get("Lang") or "").lower() for t in s}
        c["tweets_with_en"] += "en" in langs
        c["tweets_with_cstype"] += any("CSType" in t.misc for t in s)
        c["tweets_with_correctform"] += any("CorrectForm" in t.misc for t in s)
        for t in s:
            lg = (t.misc.get("Lang") or "").lower()
            if lg:
                c["lang_tagged"] += 1
                c["lang_en"] += lg == "en"
            if t.upos == "SYM":
                c["sym"] += 1
            if t.upos in ("PUNCT", "SYM"):
                continue
            c["words_gold"] += 1
            if "CorrectForm" in t.misc:
                c["correctform"] += 1
                if classify_correction(t.form, t.misc["CorrectForm"]) == "diacritic_only":
                    c["correctform_diacritic"] += 1
            if not is_word(t.form):
                continue
            c["words"] += 1
            low = t.form.lower()
            c["fada_words"] += bool(FADA & set(t.form))
            c["missing_fada"] += low in lx.MISSING_FADA
            c["discourse"] += low in lx.DISCOURSE_MARKERS
            c["abbrev"] += low in lx.ABBREVIATIONS
    return c


MEASURES = [
    ("Tweets with at least one English-tagged token", "tweets_with_en", "tweets"),
    ("Tweets with a code-switch type annotation", "tweets_with_cstype", "tweets"),
    ("Tweets with at least one corrected form", "tweets_with_correctform", "tweets"),
    ("English share of language-tagged tokens", "lang_en", "lang_tagged"),
    ("SYM (emoji, symbols) share of tokens", "sym", "tokens"),
    ("Words with a corrected form", "correctform", "words_gold"),
    ("Corrected forms that differ only in diacritics", "correctform_diacritic", "correctform"),
    ("Words carrying a fada", "fada_words", "words"),
    ("Missing-fada candidates (30-word list)", "missing_fada", "words"),
    ("English discourse markers (8-word list)", "discourse", "words"),
    ("Listed initialisms (GRMA etc.)", "abbrev", "words"),
]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--twittirish", required=True)
    ap.add_argument("--out", default="results")
    a = ap.parse_args()
    groups = {"LTC": [], "NTC": []}
    for f in sorted(glob.glob(os.path.join(a.twittirish, "*.conllu"))):
        for sid, sent in read_with_ids(f):
            key = (sid or "").split("_")[0]
            if key in groups:
                groups[key].append(sent)
    t = {k: tally(v) for k, v in groups.items()}
    rows, res = [], {"n": {k: {"tweets": t[k]["tweets"], "tokens": t[k]["tokens"]} for k in t}, "measures": []}
    for label, num, den in MEASURES:
        k1, n1, k2, n2 = t["LTC"][num], t["LTC"][den], t["NTC"][num], t["NTC"][den]
        p1, p2 = 100 * k1 / n1 if n1 else None, 100 * k2 / n2 if n2 else None
        pv = two_prop_z(k1, n1, k2, n2)
        res["measures"].append({"measure": label, "LTC": [k1, n1, wilson(k1, n1)], "NTC": [k2, n2, wilson(k2, n2)], "p": pv})
        shown = "<0.0001" if pv is not None and pv < 0.0001 else pv
        rows.append(f"| {label} | {k1}/{n1} ({p1:.2f}%) | {k2}/{n2} ({p2:.2f}%) | {shown} |")
    md = "\n".join([
        "# TwittIrish sub-corpora: earlier-sampled (LTC) vs later-sampled (NTC) tweets", "",
        "Generated by `scripts/compare_cohorts.py`. LTC: tweets posted 2009-2014. NTC: 2010-2019.",
        "The periods overlap and sampling differed, so read this as a coarse contrast.",
        "p-values are two-sided two-proportion z-tests, uncorrected for 11 comparisons", 
        "(Bonferroni threshold 0.0045), and treat tokens as independent, which they are not.", "",
        f"LTC: {t['LTC']['tweets']} tweets, {t['LTC']['tokens']} tokens. NTC: {t['NTC']['tweets']} tweets, {t['NTC']['tokens']} tokens.", "",
        "| Measure | LTC (2009-2014) | NTC (2010-2019) | p |", "|---|---:|---:|---:|", *rows, ""])
    os.makedirs(a.out, exist_ok=True)
    with open(os.path.join(a.out, "cohort_comparison.json"), "w", encoding="utf-8") as fh:
        json.dump(res, fh, ensure_ascii=False, indent=2)
    with open(os.path.join(a.out, "cohort_comparison.md"), "w", encoding="utf-8") as fh:
        fh.write(md)
    print(md)


if __name__ == "__main__":
    main()
