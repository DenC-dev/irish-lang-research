# Gap register

*Version 0.4, 16 November 2026. Extends section 9 of [`overview.md`](overview.md). Sources not in the overview's bibliography are listed in [`evolution.md`](evolution.md). "Not found" means my searches did not turn it up, which is weaker than "does not exist".*

Gaps 1 to 5 were in version 0.1 and are restated briefly. Gaps 6 to 18 are new.

## A. Data that does not exist or cannot be reached

| # | Gap | Evidence it is a gap | What would close it |
|---|---|---|---|
| 1 | No open corpus of pupils' written or typed Irish | Not found; the largest body of school writing is from the 1930s | Consented school writing samples, released as aggregates or behind access control |
| 2 | Speech data from young speakers is tiny | One first-language acquisition corpus follows a single Gaeltacht family (Cameron-Faulkner and Hickey 2011); Nic Leoid (2023) covers Conamara 10 to 13 year olds; nothing comparable for immersion pupils since Ó Duibhir's 2000s recordings | A new immersion speech corpus built to the same protocol as the Gaeltacht ones |
| 3 | No speaker background in any online corpus | TwittIrish reports no L1/L2 information | Data donation with a short background questionnaire |
| 4 | No longitudinal data | Called for again in the 2025 Gaeloideachas review | Follow one cohort from 6th class through post-primary |
| 5 | Nothing on video and private messaging platforms | Only journalism found | Consent-based collection; public Bluesky stream as a partial substitute (Salimi et al. 2025), untested for Irish |
| 6 | **Twitter-era corpora are frozen** | Free research access ended; the newest annotated tweets are from 2019; no open Irish tweet collection after 2019 was found | `scripts/collect_posts.py` (paid official access, yearly totals only), not yet run |
| 7 | **Irish-medium scholarship is under-indexed** | My searches run in English-language indexes; key work (for example *An Chonair Chaoch*, 2012) is in Irish and was only visible through citations | A search pass in Irish, and reading the Irish-language sources directly |

**Correction to version 0.1:** the overview said speech from young speakers was "only now being collected". That was wrong as a general statement. A small first-language acquisition corpus has existed since about 2011. The gap is its size and the absence of immersion learners.

## B. Layers of language that computational work has not touched

| # | Gap | Evidence | What would close it |
|---|---|---|---|
| 8 | **Phonology.** The best-documented new-speaker features are in pronunciation, and all the computational evidence is text | Snesareva (2017, 2018) on palatalisation; Ó Broin on urban phonetics; versus tweet corpora | Acoustic measurement of the broad/slender contrast in learner recordings already held by speech projects, with consent |
| 9 | **Syntactic complexity.** Ó Broin's finding that urban speakers use about half as many subordinate clauses has not been replicated with parsed data | Not found | Parse matched speech or writing from known speaker groups. The measure is easy: see pilot below |
| 10 | **Borrowing over time.** Hickey (2009) describes a path from switch to loanword, and nobody has tracked it in corpus data | Not found | The National Corpus of Irish plans a monitor corpus from 2000 onward, which would support this |
| 11 | **Morphological change in native speech**, such as analytic replacing synthetic verb forms, has no corpus frequency series | Described qualitatively (Ó Béarra 2007) | Same monitor corpus; dialect-tagged spoken corpus |

**Pilot for gap 9 [P]:** `scripts/clause_density.py` counts subordinate-clause relations in the two treebanks. Edited text has 17.1 per 10 sentences and tweets have 7.4 per 10 tweets, or 7.3 against 4.0 per 100 tokens (excluding predicates of *bí*). Relative clauses are about three times as frequent in edited text (1.87 against 0.64 per 100 tokens). This is a register difference between prose and tweets. It shows that tweet-length writing would understate anyone's syntactic range, so a fair test of Ó Broin's claim needs longer texts from known speakers.

## C. Effects of technology that nobody has measured

| # | Gap | Evidence | What would close it |
|---|---|---|---|
| 12 | **Training-data provenance.** No audit of how much Irish LLM training text was written by non-fluent editors or by machine translation | Most of the Irish Wikipedia was reportedly written by two non-fluent editors (The Journal 2025); web crawls are described as heavily polluted with machine translation (Scannell n.d.); gaBERT and UCCIX use Wikipedia and crawl data; eSTÓR now filters for quality (Walsh et al. 2025) | Sample and hand-rate the training sources; publish the share by source |
| 13 | **Invented words.** LLMs create Irish-looking words when translating (Castilho et al. 2025), and nobody tracks whether these enter circulation | Not found | Monitor learner and web text for the catalogued forms |
| 14 | **Synthetic voices as pronunciation models.** A widely used learning app reportedly moved to synthetic Irish audio that learners say lacks the broad/slender contrast | Anecdotal only (learner blogs) | Phonetic evaluation of commercial Irish voices; a learner outcome study |
| 15 | **Keyboards and predictive text.** Irish predictive text has existed since 2008, and its effect on spelling has not been studied | Not found. The cohort pilot in `evolution.md` shows fada marking rising between the earlier and later tweet samples, which fits a keyboard effect but does not prove one | Typing experiment with and without Irish keyboard support |
| 16 | **Generative AI in Irish-medium classrooms.** Policy bodies flag a "divide for Gaelscoileanna" and Northern Ireland has issued guidance, with no empirical study of what pupils and teachers do | AI Advisory Council (2025); not found otherwise. The portion of the 2025 Gaeloideachas review that I read does not discuss digital technology | Survey plus classroom observation |
| 17 | **Model errors against learner errors.** Irish-BLiMP shows models and fluent humans fail on different contrasts, and nobody has compared model error profiles with learner error profiles | Not found | Run Irish-BLiMP categories against the error categories in Ó Duibhir's corpus and An Corpas Cliste |

## D. Framing and coverage

| # | Gap | Evidence | What would close it |
|---|---|---|---|
| 18 | **Northern Ireland is under-served on every axis** | Fastest-growing sector (1,602 pupils in 2001, 7,811 in 2025); Ulster Irish gets the worst speech-recognition accuracy even with balanced training data (Lonergan et al. 2023b); most text resources lean on the standard and on Connacht and Munster material | Ulster-weighted data collection; evaluation sets split by dialect |

Three further points that are cautions more than gaps:

- **The growth premise is out of date.** Enrolment in the Republic fell between 2019/20 and 2023/24. Work that assumes an expanding new-speaker population should check current figures.
- **Annotation comparability.** In the cohort pilot, tweets with a code-switch label drop by more than half between sub-corpora while tweets containing English drop by about a sixth. Some "change over time" in annotated corpora is change in annotators.
- **Direction of drift.** The same pilot suggests public Irish on Twitter moved toward the standard in the 2010s. Claims that the internet is eroding written Irish need evidence of their own.

## Where a new study would add most

Ranked by how much is missing against how feasible the work is from outside Ireland:

1. **Gap 17** (model errors against learner errors). Uses only published benchmarks and published error categories. No new human data.
2. **Gap 12** (training-data audit). Public data, needs a fluent rater.
3. **Gap 9** (syntactic complexity). Needs longer texts with known speaker background, so it depends on a partner.
4. **Gaps 1 to 4 and 16.** Highest value and need ethics approval and partners in Irish-medium education.
