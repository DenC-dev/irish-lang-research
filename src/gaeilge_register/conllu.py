"""Minimal CoNLL-U reader (no dependencies)."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Token:
    form: str
    lemma: str
    upos: str
    feats: dict
    misc: dict


def _kv(field: str) -> dict:
    out = {}
    if field and field != "_":
        for part in field.split("|"):
            if "=" in part:
                k, v = part.split("=", 1)
                out[k] = v
    return out


def read_sentences(path):
    """Yield lists of Token, skipping multiword ranges and empty nodes."""
    sent = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if not line:
                if sent:
                    yield sent
                    sent = []
                continue
            if line.startswith("#"):
                continue
            cols = line.split("\t")
            if len(cols) != 10 or not cols[0].isdigit():
                continue
            sent.append(Token(cols[1], cols[2], cols[3], _kv(cols[5]), _kv(cols[9])))
    if sent:
        yield sent
