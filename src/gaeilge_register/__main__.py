"""CLI: python -m gaeilge_register FILE [FILE ...]  (or stdin)."""
import argparse
import json
import sys

from .features import analyse


def main(argv=None):
    p = argparse.ArgumentParser(prog="gaeilge_register", description=__doc__)
    p.add_argument("files", nargs="*", help="UTF-8 text files; stdin if omitted")
    p.add_argument("--rates-only", action="store_true")
    a = p.parse_args(argv)
    texts = (
        {f: open(f, encoding="utf-8").read() for f in a.files}
        if a.files
        else {"<stdin>": sys.stdin.read()}
    )
    out = {}
    for name, text in texts.items():
        rep = analyse(text)
        out[name] = rep.per_1000_words() if a.rates_only else rep.to_dict()
    json.dump(out, sys.stdout, ensure_ascii=False, indent=2)
    print()


if __name__ == "__main__":
    main()
