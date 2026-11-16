#!/usr/bin/env python3
"""Every mutation context the edited treebank supports, applied to tweets.

Version 0.3 tested a handful of hand-picked triggers. This script derives the
contexts from data instead:

  1. In the TRAINING part of UD Irish-IDT, group every eligible word by
     (previous word or previous two words, part of speech, initial class).
  2. Keep contexts where lenition, or eclipsis, is written at least 95% of the
     time on at least 20 occasions. These are the contexts where the edited
     language is near-categorical.
  3. Count what is written in those contexts in held-out edited text (IDT dev
     and test) and in tweets (TwittIrish), with three outcomes: the expected
     mutation, the other mutation (kept apart because, for example, Ulster
     Irish lenites where the standard eclipses), or no mutation.

Aggregate counts only. No tweet text is written out.

    python3 -I scripts/mutation_contexts.py --idt external/UD_Irish-IDT \
        --twittirish external/UD_Irish-TwittIrish --out results
"""
import argparse
import collections
import glob
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))

from compare_cohorts import read_with_ids, two_prop_z  # noqa: E402
from compare_treebanks import wilson  # noqa: E402
from gaeilge_register.features import is_word  # noqa: E402

TARGET_UPOS = {"NOUN", "ADJ", "VERB"}
ECL_PREFIX = (("bhf", "f"), ("mb", "b"), ("gc", "c"), ("nd", "d"), ("ng", "g"), ("bp", "p"), ("dt", "t"))
LENITABLE = set("bcdfgmpst")
ECLIPSABLE = set("bcdfgpt")
MIN_N, MIN_RATE = 20, 0.95


def surface(form):
    """Return (state, base_initial) with state in none / len / ecl."""
    w = form.lower()
    for pre, base in ECL_PREFIX:
        if w.startswith(pre):
            return "ecl", base
    if len(w) > 1 and w[1] == "h" and w[0] in LENITABLE:
        return "len", w[0]
    return "none", w[:1]


def eligible(form, base, kind):
    w = form.lower()
    if kind == "len":
        if base not in LENITABLE:
            return False
        # s is not lenited before these consonants
        rest = w[2:3] if w[1:2] == "h" else w[1:2]
        return not (base == "s" and rest in set("cfmptv"))
    return base in ECLIPSABLE


def init_class(base):
    return "dt" if base in "dt" else ("s" if base == "s" else "other")


def instances(sents, skip_foreign=True):
    """Yield (uni_key, bi_key, state, base, foreign, sid) for eligible targets."""
    for sid, s in sents:
        for i in range(1, len(s)):
            t = s[i]
            if t.upos not in TARGET_UPOS or not is_word(t.form) or len(t.form) < 2:
                continue
            p1 = s[i - 1]
            if not is_word(p1.form):
                continue
            state, base = surface(t.form)
            foreign = t.feats.get("Foreign") == "Yes" or (t.misc.get("Lang") or "ga").lower() != "ga"
            cls = init_class(base)
            uni = (p1.form.lower(), t.upos, cls)
            bi = None
            if i >= 2 and is_word(s[i - 2].form):
                bi = (s[i - 2].form.lower() + " " + p1.form.lower(), t.upos, cls)
            yield uni, bi, state, base, t.form, foreign, sid, t


def learn(train):
    tallies = {"len": collections.defaultdict(collections.Counter), "ecl": collections.defaultdict(collections.Counter)}
    agree = collections.Counter()
    for uni, bi, state, base, form, foreign, _sid, tok in instances(train):
        if foreign:
            continue
        gold = tok.feats.get("Form", "")
        gold_state = "len" if "Len" in gold else ("ecl" if "Ecl" in gold else "none")
        agree["n"] += 1
        agree["same"] += gold_state == state
        for kind in ("len", "ecl"):
            if eligible(form, base, kind):
                for key in (uni, bi):
                    if key:
                        tallies[kind][key][state] += 1
    chosen = {}
    for kind, d in tallies.items():
        chosen[kind] = {}
        for key, c in d.items():
            n = sum(c.values())
            if n >= MIN_N and c[kind] / n >= MIN_RATE:
                chosen[kind][key] = {"n": n, "rate": round(c[kind] / n, 4)}
    return chosen, agree


def evaluate(sents, chosen, group=lambda sid: "all"):
    out = collections.defaultdict(lambda: {"len": collections.Counter(), "ecl": collections.Counter()})
    for uni, bi, state, base, form, foreign, sid, _tok in instances(sents):
        for kind in ("len", "ecl"):
            if not eligible(form, base, kind):
                continue
            # most specific qualifying context wins
            key = bi if bi in chosen[kind] else (uni if uni in chosen[kind] else None)
            if key is None:
                continue
            c = out[group(sid)][kind]
            if foreign:
                c["foreign_excluded"] += 1
                continue
            c["contexts"] += 1
            other = "ecl" if kind == "len" else "len"
            c["expected" if state == kind else ("other_mutation" if state == other else "unmarked")] += 1
    return out


def summarise(c):
    n = c["contexts"]
    return {
        "contexts": n,
        "expected": c["expected"],
        "other_mutation": c["other_mutation"],
        "unmarked": c["unmarked"],
        "unmarked_pct": round(100 * c["unmarked"] / n, 2) if n else None,
        "unmarked_ci95": wilson(c["unmarked"], n),
        "other_mutation_pct": round(100 * c["other_mutation"] / n, 2) if n else None,
        "foreign_targets_excluded": c["foreign_excluded"],
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--idt", required=True)
    ap.add_argument("--twittirish", required=True)
    ap.add_argument("--out", default="results")
    a = ap.parse_args()

    def load(folder, pattern):
        sents = []
        for f in sorted(glob.glob(os.path.join(folder, pattern))):
            sents.extend(read_with_ids(f))
        return sents

    train = load(a.idt, "*-train.conllu")
    held = load(a.idt, "*-dev.conllu") + load(a.idt, "*-test.conllu")
    tw = load(a.twittirish, "*.conllu")
    chosen, agree = learn(train)
    res = {
        "selection": {"min_n": MIN_N, "min_rate": MIN_RATE,
                      "lenition_contexts": len(chosen["len"]), "eclipsis_contexts": len(chosen["ecl"]),
                      "surface_vs_gold_agreement_pct": round(100 * agree["same"] / agree["n"], 2),
                      "surface_vs_gold_n": agree["n"]},
        "contexts": {k: sorted(([" + ".join(key[:1]), key[1], key[2], v["n"], v["rate"]] for key, v in d.items()),
                               key=lambda r: -r[3]) for k, d in chosen.items()},
        "IDT_heldout": {k: summarise(v) for k, v in evaluate(held, chosen)["all"].items()},
        "TwittIrish": {k: summarise(v) for k, v in evaluate(tw, chosen)["all"].items()},
    }
    by = evaluate(tw, chosen, group=lambda sid: (sid or "").split("_")[0])
    res["TwittIrish_by_sample"] = {g: {k: summarise(v) for k, v in d.items()} for g, d in sorted(by.items())}
    for kind in ("len", "ecl"):
        l, n = by["LTC"][kind], by["NTC"][kind]
        res["TwittIrish_by_sample"][f"p_{kind}_unmarked"] = two_prop_z(l["unmarked"], l["contexts"], n["unmarked"], n["contexts"])

    os.makedirs(a.out, exist_ok=True)
    with open(os.path.join(a.out, "mutation_contexts.json"), "w", encoding="utf-8") as fh:
        json.dump(res, fh, ensure_ascii=False, indent=2)

    def row(label, d):
        return (f"| {label} | {d['contexts']} | {d['expected']} | {d['other_mutation']} ({d['other_mutation_pct']}%) "
                f"| {d['unmarked']} ({d['unmarked_pct']}%) | {d['unmarked_ci95']} | {d['foreign_targets_excluded']} |")

    head = ["| Data | Contexts | Expected mutation | Other mutation | No mutation | 95% interval, no mutation (%) | Non-Irish targets left out |",
            "|---|---:|---:|---:|---:|---:|---:|"]
    s = res["selection"]
    md = ["# Mutation in every near-categorical context", "",
          "Generated by `scripts/mutation_contexts.py`. Aggregate counts only.", "",
          f"Contexts were learned from the training part of UD Irish-IDT: previous word (or previous two words), "
          f"part of speech of the target (noun, adjective, verb) and initial class, kept when the mutation is written "
          f"at least {int(MIN_RATE*100)}% of the time on at least {MIN_N} occasions.", "",
          f"- Lenition contexts kept: {s['lenition_contexts']}",
          f"- Eclipsis contexts kept: {s['eclipsis_contexts']}",
          f"- Agreement between the spelling-based detector and the treebank's own mutation tags: "
          f"{s['surface_vs_gold_agreement_pct']}% of {s['surface_vs_gold_n']} words", ""]
    for kind, name in (("len", "Lenition"), ("ecl", "Eclipsis")):
        md += [f"## {name}", "", *head,
               row("Edited text, held out (IDT dev and test)", res["IDT_heldout"][kind]),
               row("Tweets (TwittIrish, all)", res["TwittIrish"][kind]),
               row("Tweets, earlier sample (2009 to 2014)", res["TwittIrish_by_sample"]["LTC"][kind]),
               row("Tweets, later sample (2010 to 2019)", res["TwittIrish_by_sample"]["NTC"][kind]),
               "", f"Earlier against later, no mutation: p = {res['TwittIrish_by_sample'][f'p_{kind}_unmarked']}", ""]
    md += ["## Contexts kept (ten most frequent of each kind)", ""]
    for kind, name in (("len", "Lenition"), ("ecl", "Eclipsis")):
        md.append(f"{name}: " + "; ".join(f"*{c[0]}* + {c[1]} ({c[2]}-initial), n={c[3]}" for c in res["contexts"][kind][:10]))
        md.append("")
    md += ["The full list is in `mutation_contexts.json`.", ""]
    text = "\n".join(md)
    with open(os.path.join(a.out, "mutation_contexts.md"), "w", encoding="utf-8") as fh:
        fh.write(text)
    print(text)


if __name__ == "__main__":
    main()
