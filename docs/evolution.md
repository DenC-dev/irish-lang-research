# How it has evolved: the language, the schools, the technology and the research

*Version 0.2 addition, 16 November 2026. Companion to [`overview.md`](overview.md); evidence labels as defined there ([E] established, [P] pilot from this repository, [H] hypothesis, [A] anecdotal). New references are listed at the end.*

Four things have changed at once, at different speeds, and most confusion about "new Irish" comes from mixing them up.

## 1. The written norm (1945 to now)

- **[E]** Spelling was reformed in 1945 to 1947 and grammar guidance followed in 1953. The two were combined as *An Caighdeán Oifigiúil* in 1958 (Wikipedia, "An Caighdeán Oifigiúil"; Scannell 2014).
- **[E]** The standard then stood almost unrevised for over fifty years. Revised editions appeared in 2012 and 2017, and review is now required at least every seven years. The revisions moved some recommendations closer to Gaeltacht speech, for example by accepting the nominative in more places where the genitive was historically required.
- **[E]** Pre-standard spelling is far enough from modern spelling that NLP tools need a normalisation step to read it (Scannell 2014; Dereza et al. 2023, on texts from 1581 to 1926).

Why it matters here: every "non-standard" count in this repository is measured against a norm that is itself about seventy years old, was a compromise between dialects, and has recently moved toward usage.

## 2. Who learns Irish, and where (1972 to now)

| Year | Irish-medium provision outside the Gaeltacht (Republic unless stated) | Source |
|---|---|---|
| 1972 | 11 primary and 5 post-primary schools | Wikipedia, "Gaelscoil", citing Gaeloideachas |
| 2015/16 | 144 primaries (35,850 pupils), 42 post-primary (11,008) | Hickey 2016 |
| 2018/19 | 147 primaries with almost 38,000 pupils | Irish Times 2019 |
| 2019/20 | 48,518 pupils, primary and post-primary together | Irish Times 2024a |
| 2023/24 | 46,933 pupils, the first fall in fifty years | Irish Times 2024a, 2024b |
| Nov 2025 | 151 primaries and 29 post-primary schools; first State policy for Irish-medium education outside the Gaeltacht | Irish Times 2025; Gaeloideachas 2025b |
| Northern Ireland | 1,602 pupils in 2001, 7,811 in 2025 | Dearg 2025 |

- **[E]** The sector grew from a parent-led movement for five decades and has now plateaued in the Republic while still growing fast in Northern Ireland. About 6.7% of primary pupils outside the Gaeltacht attend Irish-medium schools (Irish Times 2024b).
- The two post-primary counts differ (42 against 29), probably because one includes Irish-medium units inside English-medium schools. I have not reconciled them.
- **Consequence [H]:** the picture of an ever-growing pool of school-made speakers needs updating. The cohorts who were in Gaelscoileanna in the 1990s and 2000s are now the adults writing Irish online, and the cohorts behind them are no longer larger.

## 3. The spoken language

### In the Gaeltacht

- **[E]** Younger traditional speakers favour analytic verb forms (*bheadh mé*) over the synthetic forms (*bheinn*) of older speakers, one of several generational shifts described by Ó Béarra (2007).
- **[E]** English discourse markers are long established in native speech. Among ten native-speaker preschool leaders, 78% of intrasentential switches came from a small set of discourse markers (Hickey 2009). Hickey describes a path from one-off switch to borrowing to loanword that may displace the Irish form.
- **[E]** Among Conamara speakers aged 10 to 13, Irish with code-switching was the norm, and it did not disturb Irish syntax or the flow of speech (Nic Leoid 2023).
- **[E]** Grammatical gender marking and vocabulary are weakening under reduced input (Nic Fhlannchadha and Hickey 2021; Péterváry et al. 2014).

### Outside the Gaeltacht

- **[E]** The best-documented differences are in sound. Dublin new speakers tend to lose the contrast between palatalised and non-palatalised consonants, with palatalisation becoming tied to the neighbouring vowel as a tendency (Snesareva 2017, 2018).
- **[E, single study reported in the press by its author]** Comparing radio newsreaders, Ó Broin found Gaeltacht speakers producing about 15 subordinate clauses per 10 sentences against 6 to 8 for urban speakers, with similar vocabulary size and English never above 4% of any speaker's words (Ó Broin 2010, 2013). He raises "pidgin" and "creole" as possible labels. Those terms are contested, and section 3 of the overview explains why this repository avoids them.

**The key asymmetry:** the changes that linguists have documented most firmly in new-speaker Irish are phonological and syntactic-complexity changes in speech. The computational evidence is almost entirely about spelling and vocabulary in writing. The two literatures are measuring different layers.

## 4. The technology

| When | What changed | Status |
|---|---|---|
| 2000s | Rule-based spelling and grammar checking (GaelSpell, An Gramadóir); 30m-word New Corpus for Ireland (2006) | E |
| 2008 to 2009 | First Irish predictive text on phones (Samsung handset, then the Vodafone and Foras na Gaeilge *Téacs* service with 25,000 words) | E (RTÉ Archives; Irish Times 2009) |
| 2010 to 2011 | Automatic diacritic restoration as a web service; Indigenous Tweets begins cataloguing Irish-language Twitter | E / recalled date |
| 2014 | Duolingo Irish launches; learners dispute whether the recorded voice is native | A (forum posts) |
| 2015 to 2022 | Annotated tweet corpora, code-switching annotation, TwittIrish treebank, gaBERT | E |
| Dec 2022 | Digital Plan for the Irish Language published | E |
| 2022 to 2023 | Duolingo replaces recorded Irish audio with synthetic voices, criticised for missing the broad/slender contrast | A (learner blogs) |
| 2023 | Free research access to Twitter data ends | E (Salimi et al. 2025) |
| 2024 | First Irish LLM (UCCIX); National Corpus of Irish launched with 101m words | E |
| Jan 2025 | Report that most of the Irish Wikipedia was written by two editors without fluent Irish; a volunteer group has since been correcting it | E for the report (The Journal 2025) |
| Feb 2025 | Government AI Advisory Council warns that weak generative-AI support for Irish creates a divide for Gaelscoileanna | E |
| 2025 | Evaluation turn: Irish-BLiMP; IRLBench (best model 76.2% in English against 55.8% in Irish, answering in Irish under 80% of the time); studies of LLM-invented Irish words (Castilho et al. 2025) and of LLM handling of hard Irish constructions (Clifford et al. 2025); eSTÓR curates vetted Irish text for MT | E |
| 2026 | Qomhrá; Northern Ireland guidance on generative AI that includes Irish-medium use cases; National Corpus by-products (shuffled sentences, embeddings) released | E |

Two shifts stand out.

1. **From helping people write the standard to generating Irish for them.** Until about 2022 the tools checked, restored accents or predicted the next word. Since then they produce whole texts and voices. The first kind of tool pushes writers toward the norm. The second kind supplies a model of the language whose quality depends on training data that fluent speakers describe as heavily polluted with machine translation and uneven Wikipedia text (Scannell n.d.).
2. **From building to evaluating.** The 2025 papers are the first to ask systematically what kind of Irish the models produce.

## 5. The research

- **Immersion research:** from Macnamara's 1966 attainment study and its critics, through attitude and achievement surveys, to corpus description of pupil speech (Ó Duibhir 2009) and then classroom interventions (2016 to 2023). A 2025 review commissioned by Gaeloideachas describes a broadening toward metalinguistic skills, executive function, biliteracy, disadvantage and multilingual classrooms, and repeats calls for longitudinal work (Gaeloideachas 2025a; I read roughly the first third).
- **Sociolinguistics:** from "semi-speaker" and deficit vocabulary toward the "new speaker" framework in the 2010s, which studies legitimacy and practice.
- **NLP:** rule-based, then statistical, then neural, then pretrained models, then LLMs. User-generated text entered in 2015 and dialect awareness arrived first in speech technology (Lonergan et al. 2023a, 2023b).
- **What never happened:** the three strands have not shared data. The immersion corpus is not public, the tweet corpora carry no speaker background, and the learner corpus does not flag school type.

## 6. Pilot: did Irish tweets change between the earlier and later samples? [P]

TwittIrish combines two samples: LTC (tweets posted 2009 to 2014) and NTC (2010 to 2019). `scripts/compare_cohorts.py` compares them. Full table in [`results/cohort_comparison.md`](../results/cohort_comparison.md).

| Measure | Earlier sample (LTC) | Later sample (NTC) |
|---|---:|---:|
| Missing-fada candidates, share of words | 0.52% | 0.16% |
| Words carrying a fada | 24.7% | 27.9% |
| Words given a corrected form by annotators | 3.03% | 1.71% |
| English share of language-tagged tokens | 6.56% | 5.23% |
| Emoji and symbols, share of tokens | 3.94% | 5.67% |

- The later sample sits **closer** to standard spelling and has less English, while using more emoji. All five differences have p below 0.0001 on a simple test that overstates certainty because tokens within a tweet are not independent.
- The two fada rows do not depend on annotation, so they are the most trustworthy. The corrected-form and code-switching rows may partly reflect different annotators: tweets with a code-switch label fall by more than half between samples while tweets containing English fall only from 24.4% to 20.2%.
- **Possible explanations [H]:** better phone keyboards and Irish predictive text; a larger share of institutional or professional accounts later on; different sampling (from tweets in LTC, from a user database in NTC). The data cannot separate these.
- **What it argues against:** a simple story in which online Irish drifts steadily away from the standard. On this evidence, public Irish on Twitter became more standard-like during the 2010s.

## 7. Pilot: clause density in edited text and tweets [P]

See gap 9 in [`gaps.md`](gaps.md) and [`results/clause_density.md`](../results/clause_density.md). Edited prose has roughly twice the subordinate-clause density of tweets. That is a register effect, and it means short-form online text is a poor place to test claims about syntactic simplification.

## Additional references

† = identified from a record or abstract, not read in full.

- Castilho, S. et al. (2025). Hallucinations, confabulations, and the creation of Irish words in LLM-generated translations. *MT Summit 2025*. † <https://aclanthology.org/2025.mtsummit-1.22.pdf>
- Clifford, T. et al. (2025). Gaeilge Bhriste ó Shamhlacha Cliste: how clever are LLMs when translating Irish text? *CLTW 5*. † <https://aclanthology.org/2025.cltw-1.5/>
- Dearg (2025). Number of children in Irish-language education rises by 400%. (News.) <https://www.dearg.ie/en/nuacht/cartlann/135636-ime-rises-400>
- Dereza, O., Fransen, T. and McCrae, J. P. (2023). Temporal domain adaptation for historical Irish. *VarDial 2023*. † (Co-authors recalled.) <https://aclanthology.org/2023.vardial-1.6/>
- Gaeloideachas (2025a). *Immersion Education at Primary Level in Ireland* (research review). <https://gaeloideachas.ie/wp-content/uploads/2025/07/Immersion-Education-at-Primary-Level-in-Ireland.pdf>
- Gaeloideachas (2025b). Policy for Irish-Medium Education: much work to be done. Press statement, 6 November 2025. <https://gaeloideachas.ie/policy-for-irish-medium-education-much-work-to-be-done-to-realise-the-vision-of-the-department-of-education-and-youth/>
- Government of Ireland AI Advisory Council (2025). *AI and Education*, advice paper, February 2025. <https://enterprise.gov.ie/en/publications/publication-files/ai-advisory-council-ai-on-education-paper.pdf>
- Hickey, T. M. (2009). Code-switching and borrowing in Irish. *Journal of Sociolinguistics* 13, 670-688. <http://hdl.handle.net/10197/4792>
- Irish Times (2009). Predictive texting "as Gaeilge" now available. <https://www.irishtimes.com/news/predictive-texting-as-gaeilge-now-available-1.1237074>
- Irish Times (2019). Number of primary school pupils taught through Irish at record level. <https://www.irishtimes.com/news/education/number-of-primary-school-pupils-taught-through-irish-at-record-level-1.4011570>
- Irish Times (2024a). "He is completely fluent in Irish and it would be an awful shame to lose that." 29 April 2024. <https://www.irishtimes.com/ireland/education/2024/04/29/he-is-completely-fluent-in-irish-and-it-would-be-an-awful-shame-to-lose-that>
- Irish Times (2024b). Our Government aspires to boost education through Irish, yet student numbers have fallen for the first time in 50 years. 5 November 2024. <https://www.irishtimes.com/ireland/education/2024/11/05/our-government-aspires-to-boost-education-through-irish-yet-student-numbers-have-fallen-for-the-first-time-in-50-years>
- Irish Times (2025). Irish-language education policy "ignores elephant in the room", advocacy groups warn. 7 November 2025. <https://www.irishtimes.com/politics/2025/11/07/irish-language-education-policy-ignores-elephant-in-the-room-advocacy-groups-warn>
- Lonergan, L. et al. (2023b). Towards spoken dialect identification of Irish. *SIGUL 2023*. <https://arxiv.org/abs/2307.07436>
- Nic Leoid, N. (2023). *Structure and functions of Irish-English codeswitching as used by young Conamara Gaeltacht speakers*. PhD thesis, University of Edinburgh. † <https://era.ed.ac.uk/handle/1842/41059>
- Ó Béarra, F. (2007). Late Modern Irish and the dynamics of language change and language death. In H. L. C. Tristram (ed.), *The Celtic Languages in Contact*, 260-269. Potsdam University Press. <https://publishup.uni-potsdam.de/files/1750/260_269.pdf>
- Ó Broin, B. (2010). Schism fears for Gaeilgeoirí. *Irish Times*, 16 January 2010. <https://www.irishtimes.com/life-and-style/people/schism-fears-for-gaeilgeoiri-1.1269494>
- Ó Broin, B. (2013). The changing Irish language demographic. *MultiLingual* 135. † <https://sacsanua.blogspot.com/2013/04/the-changing-irish-language-demographic.html>
- Salimi, Fatemi and Laitinen (2025). New sources of large-scale evidence: introducing a real-time global Bluesky stream. Conference abstract. <https://uefconnect.uef.fi/wp-content/uploads/2024/12/Salimi_Fatemi_Laitinen_abstract_Methods_XIX.pdf>
- Scannell, K. (n.d.). Slides on minority languages, Wikipedia quality and LLM training data. <https://docs.google.com/presentation/d/13rAl4f5BiholQ3P-AF1PWTwMNSxTW9a8/htmlpresent>
- Snesareva, M. (2017). Palatalisation in Dublin Irish, or how to speak Irish with a Dublin accent. *Studia Celtica Posnaniensia* 2(1), 63-80. <https://doi.org/10.1515/scp-2017-0004>
- Snesareva, M. (2018). Drifting towards ambiguity: a closer look at palatalisation in L2 Irish. *Studia Celto-Slavica* 8, 55-69. <https://ulster.ac.uk/celtoslavica/series/08/07>
- The Journal (2025). Most of the Irish-language Wikipedia was written by editors who did not speak Irish. January 2025. <https://thejournal.ie/gaeilge-wikipedia-written-by-editors-who-did-not-speak-irish-6589572-Jan2025/>
- RTÉ Archives. Predictive text as Gaeilge. <https://www.rte.ie/archives/2019/0124/1025237-predictive-text-as-gaeilge>
- Walsh, A. et al. (2025). eSTÓR: curating Irish datasets for machine translation. *MT Summit 2025*, vol. 2, 115-116. †
- Wikipedia. "An Caighdeán Oifigiúil" and "Gaelscoil". (Tertiary; used for dates and the 1972 school count. Check against the Oireachtas and Gaeloideachas originals.)
- Cameron-Faulkner, T. and Hickey, T. (2011). Form and function in Irish child directed speech. *Cognitive Linguistics* 22(3), 569-594. Corpus: <https://talkbank.org/childes/access/Celtic/Irish/Gaeltacht.html>
