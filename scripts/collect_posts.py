#!/usr/bin/env python3
"""Collect recent Irish-language posts and keep only yearly totals.

Why this exists: the public tweet treebank stops in 2019. This script lets the
project owner extend the series to the present using their own API access.

STATUS: written against the X API v2 and Bluesky documentation and exercised
only with the fake data in tests/test_collect.py. It has NOT been run against
either live service, because the environment it was written in cannot reach
them. Expect to adjust endpoint details.

Risk controls built in:
  * post text, post ids and account names are held in memory only and never
    written to disk; the only output is a table of yearly totals;
  * @mentions, URLs and hashtags are removed before analysis;
  * a year with fewer than --min-posts posts is suppressed, not reported;
  * the X route prints a cost estimate and stops unless --yes-spend is given;
  * credentials come from environment variables, never from arguments or files;
  * posts that do not look like Irish are dropped (platform language tags for
    Irish are unreliable).

Before running: check that your use fits the platform's current developer
terms and your university's rules for research with public social media data.

Examples:
  X_BEARER_TOKEN=... python3 scripts/collect_posts.py --source x \
      --from-year 2020 --to-year 2026 --per-year 2000 --yes-spend
  BSKY_HANDLE=... BSKY_APP_PASSWORD=... python3 scripts/collect_posts.py \
      --source bluesky --from-year 2023 --to-year 2026 --per-year 2000
"""
import argparse
import collections
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))

from gaeilge_register.features import analyse, mutation_context_counts, tokenise  # noqa: E402

X_COST_PER_POST_USD = 0.005  # reported pay-per-use read price, 2026; check your console
IRISH_COMMON = frozenset(
    """agus an ar tá is na go le sé sí mé tú bhí níl ag seo sin atá mar ach nach leis
    faoi don den sa san ó do mo ár raibh beidh inniu anois freisin maith""".split()
)
SCRUB = re.compile(r"https?://\S+|[@#]\w+")


def looks_irish(text, min_words=4, min_share=0.15):
    words = [t.lower() for t in tokenise(text) if t[:1].isalpha()]
    if len(words) < min_words:
        return False
    return sum(w in IRISH_COMMON for w in words) / len(words) >= min_share


def get_json(url, headers=None, data=None, retries=3):
    req = urllib.request.Request(url, headers=headers or {}, data=data)
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt + 1 < retries:
                time.sleep(15 * (attempt + 1))
                continue
            raise SystemExit(f"request refused ({e.code}); nothing was saved")
    raise SystemExit("gave up after repeated rate limits; nothing was saved")


def fetch_x(year, limit, fetch=get_json):
    """Yield (created_at, text). Full-archive search needs that access level."""
    token = os.environ.get("X_BEARER_TOKEN")
    if not token:
        raise SystemExit("set X_BEARER_TOKEN in the environment")
    params = {"query": "lang:ga -is:retweet", "max_results": "100", "tweet.fields": "created_at",
              "start_time": f"{year}-01-01T00:00:00Z", "end_time": f"{year}-12-31T23:59:59Z"}
    got, token_next = 0, None
    while got < limit:
        if token_next:
            params["next_token"] = token_next
        url = "https://api.x.com/2/tweets/search/all?" + urllib.parse.urlencode(params)
        page = fetch(url, {"Authorization": "Bearer " + token})
        for p in page.get("data", []):
            got += 1
            yield p.get("created_at", ""), p.get("text", "")
        token_next = page.get("meta", {}).get("next_token")
        if not token_next:
            break
        time.sleep(1)


def fetch_bluesky(year, limit, fetch=get_json):
    handle, pw = os.environ.get("BSKY_HANDLE"), os.environ.get("BSKY_APP_PASSWORD")
    if not (handle and pw):
        raise SystemExit("set BSKY_HANDLE and BSKY_APP_PASSWORD (an app password) in the environment")
    sess = fetch("https://bsky.social/xrpc/com.atproto.server.createSession",
                 {"Content-Type": "application/json"},
                 json.dumps({"identifier": handle, "password": pw}).encode())
    auth = {"Authorization": "Bearer " + sess["accessJwt"]}
    seen, got = set(), 0
    for q in ("agus", "tá", "bhí", "anseo", "maith"):
        cursor = None
        while got < limit:
            params = {"q": q, "lang": "ga", "limit": "100",
                      "since": f"{year}-01-01T00:00:00Z", "until": f"{year}-12-31T23:59:59Z"}
            if cursor:
                params["cursor"] = cursor
            page = fetch("https://bsky.social/xrpc/app.bsky.feed.searchPosts?" + urllib.parse.urlencode(params), auth)
            for p in page.get("posts", []):
                h = hashlib.sha256(p.get("uri", "").encode()).digest()  # in-memory de-duplication only
                if h in seen:
                    continue
                seen.add(h)
                got += 1
                rec = p.get("record", {})
                yield rec.get("createdAt", ""), rec.get("text", "")
            cursor = page.get("cursor")
            if not cursor:
                break
            time.sleep(1)


def summarise(posts, min_posts):
    """posts: iterable of (created_at, text). Returns yearly totals only."""
    by = collections.defaultdict(collections.Counter)
    for created, text in posts:
        year = created[:4]
        clean = SCRUB.sub(" ", text)
        by[year]["fetched"] += 1
        if not year.isdigit() or not looks_irish(clean):
            continue
        r = analyse(clean)
        m = mutation_context_counts(tokenise(clean))
        c = by[year]
        c["posts"] += 1
        c["words"] += r.n_words
        c["fada_words"] += r.words_with_fada
        c["missing_fada"] += len(r.missing_fada)
        c["english_function_words"] += r.english_function_words
        c["discourse_markers"] += sum(r.discourse_markers.values())
        for k, v in m.items():
            c[k] += v
    out = {}
    for year, c in sorted(by.items()):
        if c["posts"] < min_posts:
            out[year] = {"suppressed": f"fewer than {min_posts} Irish posts"}
            continue
        w = max(c["words"], 1)
        out[year] = {
            "posts_fetched": c["fetched"], "posts_kept_as_irish": c["posts"], "words": c["words"],
            "fada_bearing_words_pct": round(100 * c["fada_words"] / w, 2),
            "missing_fada_pct_of_words": round(100 * c["missing_fada"] / w, 3),
            "english_function_words_per_1000": round(1000 * c["english_function_words"] / w, 2),
            "discourse_markers_per_1000": round(1000 * c["discourse_markers"] / w, 2),
            "lenition_contexts_mo_do": c["len_contexts"], "lenition_unmarked": c["len_unmarked"],
            "eclipsis_contexts_ar_bhur_i": c["ecl_contexts"], "eclipsis_unmarked": c["ecl_unmarked"],
        }
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", choices=["x", "bluesky"], required=True)
    ap.add_argument("--from-year", type=int, required=True)
    ap.add_argument("--to-year", type=int, required=True)
    ap.add_argument("--per-year", type=int, default=2000)
    ap.add_argument("--min-posts", type=int, default=200)
    ap.add_argument("--yes-spend", action="store_true", help="confirm the X API charge")
    ap.add_argument("--out", default="results")
    a = ap.parse_args()
    years = range(a.from_year, a.to_year + 1)
    if a.source == "x":
        est = len(years) * a.per_year * X_COST_PER_POST_USD
        print(f"Up to {len(years) * a.per_year} post reads, roughly ${est:,.2f} at ${X_COST_PER_POST_USD}/read.", file=sys.stderr)
        if not a.yes_spend:
            raise SystemExit("Add --yes-spend to go ahead. Nothing was requested.")
    fetcher = fetch_x if a.source == "x" else fetch_bluesky

    def stream():
        for y in years:
            yield from fetcher(y, a.per_year)

    res = {"source": a.source, "note": "yearly totals only; no text, ids or account names were stored",
           "years": summarise(stream(), a.min_posts)}
    os.makedirs(a.out, exist_ok=True)
    path = os.path.join(a.out, f"posts_by_year_{a.source}.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(res, fh, ensure_ascii=False, indent=2)
    print(json.dumps(res, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
