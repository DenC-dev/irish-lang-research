import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from gaeilge_register import analyse, strip_fada, tokenise  # noqa: E402

HERE = os.path.dirname(__file__)
EXAMPLES = os.path.join(HERE, "..", "data", "examples", "constructed_examples.txt")


def examples():
    out = {}
    with open(EXAMPLES, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            label, text = line.rstrip("\n").split("\t")
            out.setdefault(label, []).append(text)
    return out


class TestFeatures(unittest.TestCase):
    def setUp(self):
        self.ex = examples()

    def test_tokenise_keeps_hyphen_and_fada(self):
        self.assertEqual(tokenise("Bhí an-time againn!"), ["Bhí", "an-time", "againn", "!"])
        self.assertEqual(strip_fada("Éireann"), "Eireann")

    def test_standard_sentences_raise_no_flags(self):
        for s in self.ex["standard"]:
            r = analyse(s)
            self.assertEqual(r.lenition_candidates, [], s)
            self.assertEqual(r.eclipsis_candidates, [], s)
            self.assertEqual(r.copula_candidates, 0, s)
            self.assertEqual(r.missing_fada, [], s)

    def test_mutation_candidates(self):
        self.assertEqual(analyse(self.ex["lenition_candidate"][0]).lenition_candidates, [("mo", "cara")])
        self.assertEqual(analyse(self.ex["eclipsis_candidate"][0]).eclipsis_candidates, [("ár", "teach")])

    def test_s_clusters_and_capitals_are_not_flagged(self):
        self.assertEqual(analyse("mo scoil agus mo stór").lenition_candidates, [])
        self.assertEqual(analyse("do Twitter").lenition_candidates, [])
        self.assertEqual(analyse("I think so").eclipsis_candidates, [])

    def test_copula_candidate(self):
        self.assertEqual(analyse(self.ex["copula_candidate"][0]).copula_candidates, 1)

    def test_contact_features(self):
        r = analyse(self.ex["discourse_markers"][0])
        self.assertEqual(r.discourse_markers, {"just": 1, "like": 1, "so": 1})
        self.assertEqual(analyse(self.ex["abbreviation"][0]).abbreviations, ["GRMA"])
        self.assertEqual(analyse(self.ex["mixed_intensifier"][0]).intensifier_an_mixed, ["an-time"])
        self.assertEqual(len(analyse(self.ex["elongation"][0]).elongations), 1)

    def test_missing_fada(self):
        r = analyse(self.ex["no_fada"][0])
        self.assertEqual([w for w, _ in r.missing_fada], ["Ta", "slan"])
        self.assertEqual(r.words_with_fada, 0)

    def test_rates(self):
        r = analyse("Tá mé just anseo").per_1000_words()
        self.assertEqual(r["words"], 4)
        self.assertEqual(r["discourse_markers"], 250.0)


if __name__ == "__main__":
    unittest.main()
