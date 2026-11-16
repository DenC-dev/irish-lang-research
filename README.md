# Síneadh

*Contemporary Irish, Gaelscoileanna and the internet, from a computational linguistics angle.*

*Síneadh* is Irish for lengthening or extension. The *síneadh fada* is the length mark on a vowel, and its presence or absence turned out to be the most reliable signal in the data.

A research overview, plus a small reproducible analysis, on what computational linguistics can currently say about Irish as acquired in Irish-medium schools and Irish as written online.

## What is here

| Path | Contents |
|---|---|
| [`paper/sineadh.pdf`](paper/sineadh.pdf) | The working paper (source in `paper/sineadh.md`, build with `paper/build.sh`) |
| [`docs/index.html`](docs/index.html) | Project website, a single self-contained page. To host it on GitHub Pages, set Pages to serve the `main` branch from `/docs` |
| [`docs/overview.md`](docs/overview.md) | The overview: terms, evidence, methods and resources, limitations, gaps, bibliography. Section 10 answers "is there already a paper on this?" |
| [`docs/evolution.md`](docs/evolution.md) | How the written norm, the schools, the spoken language, the technology and the research have changed |
| [`docs/gaps.md`](docs/gaps.md) | Gap register: 18 gaps with evidence and what would close each |
| [`results/`](results/) | Pilot numbers: edited Irish against Irish tweets, earlier against later tweet samples, clause density |
| `src/gaeilge_register/` | Dependency-free Python package that extracts transparent surface features from Irish text |
| `scripts/` | `compare_treebanks.py`, `compare_cohorts.py` and `clause_density.py` regenerate the results from the two public treebanks |
| `data/examples/` | Constructed example sentences used by the tests. No attested data |
| [`ETHICS.md`](ETHICS.md) | Data rules for this project |

## Headline pilot result

After *mo/do*, a lenitable common noun is written without lenition in 3 of 474 cases in edited text and 18 of 177 cases in tweets (10.2%, 95% CI 6.5 to 15.5). The same direction holds for eclipsis after *ár/bhur/i*. This measures distance from the written standard. It does not identify learners, because speaker background is not in the data.

Second result: between the earlier (2009 to 2014) and later (2010 to 2019) tweet samples, missing-fada candidates fall from 0.52% to 0.16% of words and English tokens fall from 6.6% to 5.2%. Public Irish on Twitter moved toward the standard over the 2010s, with caveats in `docs/evolution.md`.

## Reproduce

Python 3.9 or later, standard library only.

```bash
./scripts/fetch_ud.sh                       # clones the two treebanks into external/
python3 -I scripts/compare_treebanks.py \
    --idt external/UD_Irish-IDT \
    --twittirish external/UD_Irish-TwittIrish --out results
python3 -I scripts/compare_cohorts.py --twittirish external/UD_Irish-TwittIrish --out results
python3 -I scripts/clause_density.py --idt external/UD_Irish-IDT \
    --twittirish external/UD_Irish-TwittIrish --out results
python3 -m unittest discover -s tests
```

Results in this repository were produced from UD Irish-IDT commit `c30cbaa` and UD Irish-TwittIrish commit `a52a11b`.

## Use the feature extractor

```bash
echo "Tá mé just ag caint le mo cara, GRMA" | PYTHONPATH=src python3 -m gaeilge_register
```

```python
from gaeilge_register import analyse
analyse("Tá ár teach in aice leis an scoil").eclipsis_candidates   # [('ár', 'teach')]
```

Every flag is a candidate for a person to look at. The rules assume the Caighdeán Oifigiúil, so legitimate dialect forms can be flagged, and the word lists are short and illustrative. Do not use the output to grade writing or to classify people as learners or native speakers.

## Status and limits

- The overview is a literature synthesis from one search session (16 November 2026) in English-language indexes. Entries marked † in the bibliography were not read in full.
- The pilot is descriptive, uses tweets from 2009 to 2019, and has small counts for the mutation measures.
- Nothing here has been reviewed by an Irish-language linguist. Review by a fluent speaker is the obvious next step.

## Licence

Code: MIT. Text in `docs/` and `results/`: CC BY 4.0. The treebanks are not redistributed and keep their own licences (CC BY-SA 3.0 and 4.0).
