# Contemporary Irish, Gaelscoileanna and the Internet

A research overview, plus a small reproducible analysis, on what computational linguistics can currently say about Irish as acquired in Irish-medium schools and Irish as written online.

## What is here

| Path | Contents |
|---|---|
| [`docs/overview.md`](docs/overview.md) | The overview: terms, evidence, methods and resources, limitations, gaps, bibliography. Section 10 answers "is there already a paper on this?" |
| [`results/treebank_comparison.md`](results/treebank_comparison.md) | Pilot numbers: edited Irish (UD Irish-IDT) against Irish tweets (UD TwittIrish) |
| `src/gaeilge_register/` | Dependency-free Python package that extracts transparent surface features from Irish text |
| `scripts/compare_treebanks.py` | Regenerates the results from the two public treebanks |
| `data/examples/` | Constructed example sentences used by the tests. No attested data |
| [`ETHICS.md`](ETHICS.md) | Data rules for this project |

## Headline pilot result

After *mo/do*, a lenitable common noun is written without lenition in 3 of 474 cases in edited text and 18 of 177 cases in tweets (10.2%, 95% CI 6.5 to 15.5). The same direction holds for eclipsis after *ár/bhur/i*. This measures distance from the written standard. It does not identify learners, because speaker background is not in the data.

## Reproduce

Python 3.9 or later, standard library only.

```bash
./scripts/fetch_ud.sh                       # clones the two treebanks into external/
python3 -I scripts/compare_treebanks.py \
    --idt external/UD_Irish-IDT \
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
