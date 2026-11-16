import os
import sys
import unittest

HERE = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(HERE, "..", "src"))
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))

import collect_posts as cp  # noqa: E402
from gaeilge_register import mutation_context_counts, tokenise  # noqa: E402

# Constructed posts. Not real data.
IRISH = "Bhi mo cara ag ár teach inne agus tá sé go maith @duine https://example.org #gaeilge"
STANDARD = "Bhí mo chara ag ár dteach inné agus tá sé go maith"
ENGLISH = "This is a post in English about the weather today"


class TestCollect(unittest.TestCase):
    def test_language_filter(self):
        self.assertTrue(cp.looks_irish(STANDARD))
        self.assertFalse(cp.looks_irish(ENGLISH))
        self.assertFalse(cp.looks_irish("Tá"))

    def test_context_counts(self):
        self.assertEqual(mutation_context_counts(tokenise(STANDARD)),
                         {"len_contexts": 1, "len_unmarked": 0, "ecl_contexts": 1, "ecl_unmarked": 0})
        self.assertEqual(mutation_context_counts(tokenise("mo cara i teach")),
                         {"len_contexts": 1, "len_unmarked": 1, "ecl_contexts": 1, "ecl_unmarked": 1})
        # lenition where the standard eclipses is not counted as unmarked
        self.assertEqual(mutation_context_counts(tokenise("i chuile áit"))["ecl_unmarked"], 0)

    def test_summary_holds_totals_only(self):
        posts = [("2024-03-01T10:00:00Z", IRISH)] * 3 + [("2024-03-02T10:00:00Z", ENGLISH)] + [("2025-01-01T00:00:00Z", STANDARD)]
        out = cp.summarise(posts, min_posts=2)
        self.assertEqual(out["2024"]["posts_fetched"], 4)
        self.assertEqual(out["2024"]["posts_kept_as_irish"], 3)
        self.assertEqual(out["2024"]["lenition_unmarked"], 3)
        self.assertEqual(out["2024"]["eclipsis_unmarked"], 3)
        self.assertIn("suppressed", out["2025"])
        blob = repr(out)
        for leak in ("cara", "duine", "example.org", "gaeilge"):
            self.assertNotIn(leak, blob)

    def test_x_pagination_with_fake_fetcher(self):
        os.environ["X_BEARER_TOKEN"] = "test"
        pages = [{"data": [{"created_at": "2024-01-01T00:00:00Z", "text": STANDARD}] * 2, "meta": {"next_token": "n"}},
                 {"data": [{"created_at": "2024-01-02T00:00:00Z", "text": STANDARD}], "meta": {}}]
        calls = []

        def fake(url, headers=None, data=None):
            calls.append(url)
            return pages[len(calls) - 1]

        real_sleep, cp.time.sleep = cp.time.sleep, lambda s: None
        try:
            got = list(cp.fetch_x(2024, 10, fetch=fake))
        finally:
            cp.time.sleep = real_sleep
            del os.environ["X_BEARER_TOKEN"]
        self.assertEqual(len(got), 3)
        self.assertIn("next_token=n", calls[1])
        self.assertIn("lang%3Aga", calls[0])


if __name__ == "__main__":
    unittest.main()
