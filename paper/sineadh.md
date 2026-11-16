---
title: "Síneadh: What Computational Linguistics Can and Cannot Yet Say about School-Acquired and Online Irish"
author: "Dennis Crowley (Florida State University)"
date: "Version 0.4, 16 November 2026"
abstract: |
  Irish is now acquired mainly through school and written increasingly on screens, yet the research on those two facts has developed separately. Applied linguists have described the speech of immersion pupils from classroom recordings, and computational linguists have described Irish tweets, with no shared data between them. This paper reviews both literatures, sets out what each can support, and reports descriptive analyses of two public Universal Dependencies treebanks. First, across every context where edited Irish writes lenition near-categorically, tweets leave it unwritten about eight times as often (9.5% against 1.2%). Eclipsis shows no reliable difference (0.9% against 0.0%), which corrects an earlier estimate based on a few hand-picked triggers. Second, a later sample of tweets (2010 to 2019) sits closer to standard spelling than an earlier one (2009 to 2014): candidate missing length marks fall from 0.52% to 0.16% of words. Third, tweets carry about half the subordinate-clause density of edited prose. None of these results identifies learners, because no public corpus of online Irish records speaker background. The paper closes with a register of eighteen research gaps, the most tractable of which is a comparison between the grammatical errors of language models and those of learners.
geometry: margin=1in
fontsize: 11pt
mainfont: "DejaVu Serif"
linkcolor: blue
urlcolor: blue
---

**Status.** This paper is a literature synthesis with exploratory analyses and has not been peer reviewed. The author speaks Irish. The example sentences and word lists have not yet had independent review by a second speaker. The literature search, code and drafting were carried out with an AI assistant (Claude, Anthropic) under the author's direction. Sources that were identified from abstracts or repository records and not read in full are marked † in the reference list. Code, data pointers and full outputs: <https://github.com/DenC-dev/irish-lang-research>.

**The name.** *Síneadh* means lengthening or extension. The *síneadh fada* is the length mark on Irish vowels, whose presence or absence turned out to be the most reliable signal in the data. The word also fits a language being extended into new speakers and new media.

# 1. Introduction

In the 2022 census, 623,961 people in the Republic of Ireland reported speaking Irish daily once use inside the education system is counted, and 71,968 reported speaking it daily outside education (CSO 2023). For most young users, then, Irish is something that happens at school. At the same time, much of the Irish that anyone reads or writes informally now passes through phones, platforms and, since about 2022, generative models.

These two developments raise a shared question: is a school-shaped, screen-mediated Irish emerging, and can it be measured? The question matters for teachers deciding what to correct, for engineers deciding what their tools should accept, and for a speech community in which the legitimacy of "new speakers" is openly contested (O'Rourke and Walsh 2015).

This paper makes three contributions. It brings together two literatures that rarely cite each other. It reports reproducible descriptive analyses on open data. And it catalogues what is missing, with attention to why the obvious study (comparing the online writing of immersion-educated, Gaeltacht-raised and adult-learner writers) cannot currently be done.

# 2. Background

## 2.1 Terms

Four labels are in use and they pick out different things. *Traditional* or *Gaeltacht Irish* refers to home-acquired Irish in the Ulster, Connacht and Munster dialect areas. *An Caighdeán Oifigiúil* is the written standard, assembled from spelling reforms in 1945 to 1947 and grammar guidance in 1953, published in 1958, and revised only in 2012 and 2017. *New speakers* are people who use Irish regularly without being traditional native speakers (Walsh, O'Rourke and Rowland 2015). *Gaelscoilis* and *post-Gaeltacht Irish* are labels, partly pejorative, for the speech of immersion pupils and urban speakers.

This paper avoids treating any of these as a bounded variety. There is no evidence for a uniform "Gaelscoil dialect", and native-speaker Irish is itself changing.

## 2.2 School-acquired Irish

The central dataset is a corpus of pupils talking during a collaborative task (Ó Duibhir 2009; Ó Duibhir and Garland 2010). Table 1 gives its headline figures.

| Group | Pupils | Words | Utterances with an error | English words |
|---|---:|---:|---:|---:|
| Irish-medium, Northern Ireland | 24 | 14,394 | 32.1% | 8.75% |
| All-Irish, Republic | 65 | 30,783 | 29.2% | 10.03% |
| Gaeltacht | 15 | 4,557 | 2.6% | 6.65% |

: Pupil speech corpus (Ó Duibhir and Garland 2010).

Pupils used verb-initial word order and noun-adjective order correctly. The persistent non-target features were the copula against the substantive verb (*is* against *bí*) and verbal-noun clauses. Most English material was a set of eight discourse markers (*so, right, yeah, no, just, like, then, okay*), which also dominated the English used by the Gaeltacht group. Error rates ranged from 20.5% to 41.6% across schools, which is the strongest single piece of evidence against a uniform school variety. Peer correction targeted the use of English and never an Irish form. Explicit instruction improves accuracy on targeted forms (Ó Duibhir, Ní Dhiorbháin and Cosgrove 2016).

## 2.3 Native-speaker Irish is also moving

English discourse markers are long established in native speech: among ten native-speaker preschool leaders, 78% of intrasentential switches came from a small set of them (Hickey 2009). Conamara speakers aged 10 to 13 use Irish with code-switching as their norm without disruption to Irish syntax (Nic Leoid 2023). Young Gaeltacht speakers, aged 6 to 13, show incomplete acquisition of grammatical gender under variable adult input (Nic Fhlannchadha and Hickey 2021), and pupils from Irish-only homes have been found to have stronger English than Irish (Péterváry et al. 2014). A learner/native contrast therefore cannot be read off school type or address.

## 2.4 Where new-speaker Irish differs most

The best-documented differences are in speech. Dublin new speakers tend to lose the palatalisation contrast (Snesareva 2017, 2018). Ó Broin (2010) compared radio newsreaders and reported about 15 subordinate clauses per 10 sentences for Gaeltacht speakers against six to eight for urban speakers, with similar vocabulary. That study is known mainly through the author's own press account and has not been replicated.

## 2.5 Irish online

Caulfield (2013) found Irish-language networks of roughly 150 to 300 regular participants on blogs, Twitter and Facebook, mostly adult, male and urban. In 1,496 annotated tweets, 16% contained code-switching (Lynn and Scannell 2019). The TwittIrish treebank documents omitted length marks, abbreviations such as GRMA, phonetic respellings, dialect forms and contractions, and shows that parsers trained on edited text lose 23 to 25 points of labelled attachment score on tweets (Cassidy et al. 2022). The treebank authors report no first-language or second-language breakdown, because the data contain none.

## 2.6 Tools and models

Irish has reference corpora of 30 to 101 million words (Kilgarriff et al. 2006; Ó Meachair et al. 2026), a learner corpus harvested from a writing platform (Ní Chiaráin et al. 2022), rule-based checkers built around the standard, a monolingual BERT model (Barry et al. 2022) and two Irish-adapted large language models (Tran et al. 2024; McInerney et al. 2026). On the Irish-BLiMP benchmark fluent humans score 90.1% and the best model 73.5%, and the two fail on different contrasts (McGiff et al. 2025). On IRLBench the best model reaches 76.2% in English and 55.8% in Irish (IRLBench 2025).

Two concerns about training data recur. Web crawls are described by a leading practitioner as heavily polluted with machine translation (Scannell n.d.), and most of the Irish Wikipedia was reportedly written by two editors without fluent Irish (The Journal 2025).

# 3. Data and methods

## 3.1 Data

Two public treebanks are used, neither of which is redistributed with this paper.

- **UD Irish-IDT** (commit `c30cbaa`): 4,910 sentences and 115,990 tokens of news, fiction, web, legal and government text, with morphological features including gold mutation tags.
- **UD Irish-TwittIrish** (commit `a52a11b`): 2,596 tweets and 47,790 tokens, with token-level language tags and annotator-supplied corrected forms. It combines the Lynn Twitter Corpus (LTC, 1,299 tweets posted 2009 to 2014) and the New Twitter Corpus (NTC, 1,297 tweets posted 2010 to 2019). Usernames, phone numbers and emails were anonymised by the maintainers.

## 3.2 Measures

All measures are rule-based and inspectable, and the code has no dependencies beyond the Python standard library.

- **Mutation, all supported contexts.** Contexts are learned from the training part of IDT. Every noun, adjective or verb with a mutable initial is grouped by the previous word (or previous two words), its part of speech and its initial class (*d/t*, *s*, other). A context is kept when the edited text writes lenition, or eclipsis, at least 95% of the time on at least 20 occasions. This yields 18 lenition contexts and 14 eclipsis contexts. Each occurrence in held-out edited text (IDT development and test sets) and in tweets is then given one of three outcomes: the expected mutation, the other mutation, or none. The other mutation is kept apart because some dialects lenite where the standard eclipses. Words tagged as English or foreign are left out.
- **Mutation, hand-picked triggers.** The first version of this analysis used only *mo/do* for lenition and *ár/bhur/i* for eclipsis before common nouns, and counted any word without the expected spelling as unmarked. It is reported for comparison.
- **Missing length marks.** A list of 30 frequent words whose unaccented spelling is not itself a standard Irish word (for example *ta* for *tá*). Ambiguous pairs such as *ar/ár* are excluded.
- **English material.** TwittIrish language tags, plus two short word lists (English function words; the eight discourse markers from Table 1) that can be applied to both treebanks.
- **Subordinate-clause density.** Counts of the dependency relations ccomp, xcomp, advcl, acl and csubj, excluding xcomp:pred, which in the Irish annotation marks predicates of *bí*.

Proportions are reported with 95% Wilson intervals where counts are small. Cohort differences use a two-proportion z-test, which overstates certainty because tokens within a tweet are not independent.

## 3.3 Validation

The spelling-based mutation detector agrees with the treebank's own mutation tags on 99.5% of 36,351 words. On held-out edited text the learned contexts behave as intended: lenition is written in 248 of 254 cases and eclipsis in all 295. The pipeline also reproduces published figures for TwittIrish (22.3% of tweets contain an English token, against "about 25%" multilingual tweets in Cassidy et al. 2022; 2.3% of words carry a corrected form, against 2.5% of tokens with orthographic variation).

# 4. Results

## 4.1 Edited prose against tweets

| Measure | Edited (IDT) | Tweets (TwittIrish) |
|---|---:|---:|
| Mean tokens per sentence or tweet | 23.6 | 18.4 |
| Words carrying a length mark | 31.8% | 26.3% |
| Missing-length-mark candidates per 1,000 words | 0.04 | 3.37 |
| English function words per 1,000 words | 0.68 | 11.73 |
| Eight discourse markers per 1,000 words | 0.30 | 0.84 |
| Subordinate clauses per 10 sentences or tweets | 17.1 | 7.4 |

: Surface measures applied identically to both treebanks.

In TwittIrish's own annotation, 5.9% of language-tagged tokens are English and about 41% of corrected forms differ from the written form only in diacritics.

The discourse markers that dominate pupils' speech are rare in tweets (0.84 per 1,000 words), which is consistent with a difference between speech and writing. The clause-density row is taken up in section 4.4.

## 4.2 Mutation in every supported context

| Data | Contexts | Expected | Other mutation | None (95% interval) |
|---|---:|---:|---:|---:|
| Lenition, edited held-out | 254 | 248 | 3 | 3, 1.2% (0.4 to 3.4) |
| Lenition, tweets | 388 | 349 | 2 | 37, 9.5% (7.0 to 12.9) |
| Eclipsis, edited held-out | 295 | 295 | 0 | 0, 0.0% (0.0 to 1.3) |
| Eclipsis, tweets | 424 | 416 | 4 | 4, 0.9% (0.4 to 2.4) |

: Outcomes in contexts where edited Irish mutates near-categorically.

Lenition is left unwritten in 9.5% of tweet contexts against 1.2% in held-out edited text, and the intervals do not overlap. The hand-picked *mo/do* rule gave 10.2% (18 of 177) against 0.6%, so the wider analysis confirms it on twice the data.

Eclipsis does not show a reliable difference. The hand-picked rule had suggested 5.0% unmarked in tweets (7 of 139). With all supported contexts the figure is 0.9% (4 of 424), and four further cases carry lenition, which is a legitimate pattern in some dialects and had been miscounted as unmarked. The earlier eclipsis estimate should be set aside.

Between the earlier and later tweet samples, unwritten lenition falls from 12.2% (23 of 188) to 7.0% (14 of 200). The direction matches section 4.3, and the difference is not significant at these counts (p = 0.08).

## 4.3 Earlier against later tweets

| Measure | LTC (2009 to 2014) | NTC (2010 to 2019) | p |
|---|---:|---:|---:|
| Missing-length-mark candidates, share of words | 0.52% | 0.16% | <0.0001 |
| Words carrying a length mark | 24.7% | 27.9% | <0.0001 |
| Words given a corrected form | 3.03% | 1.71% | <0.0001 |
| English share of language-tagged tokens | 6.56% | 5.23% | <0.0001 |
| Emoji and symbols, share of tokens | 3.94% | 5.67% | <0.0001 |
| Tweets containing an English token | 24.4% | 20.2% | 0.010 |
| Tweets with a code-switch label | 8.5% | 3.9% | <0.0001 |

: The two sub-corpora of TwittIrish.

The later sample is closer to standard spelling and contains less English, while using more emoji. The two length-mark rows do not depend on annotation and are the most trustworthy. The last two rows show why the annotated rows need care: labelled code-switching falls by more than half while tweets containing English fall by about a sixth, which suggests the two sub-corpora were annotated differently.

## 4.4 Clause density

| Measure | Edited (IDT) | Tweets (TwittIrish) |
|---|---:|---:|
| Subordinate clauses per 10 sentences or tweets | 17.1 | 7.4 |
| Subordinate clauses per 100 tokens | 7.25 | 4.03 |
| Relative clauses per 100 tokens | 1.87 | 0.64 |

: Subordinate-clause density.

Edited prose has about twice the clause density of tweets and about three times the rate of relative clauses.

# 5. Discussion

**Distance from the standard is measurable, and its cause is not.** Sections 4.1 and 4.2 show that transparent rules separate edited from user-generated Irish, and that the separation is specific: lenition and length marks differ, while eclipsis barely does. The same unwritten lenition could come from fast typing, autocorrect, an English noun, a dialect pattern, deliberate informality or incomplete acquisition. Text alone cannot distinguish these, and school-acquired Irish is only one candidate among six.

**The direction of drift is the surprise.** A common assumption is that online writing pulls a minority language away from its norm. On this evidence, public Irish on Twitter moved toward the standard during the 2010s. Three explanations are plausible and untested: better phone keyboards and predictive text (available for Irish since 2008), a growing share of institutional accounts, and the different sampling of the two sub-corpora.

**Short text hides syntax.** The clause-density result is a register effect. Its relevance is methodological: Ó Broin's claim about reduced subordination among urban speakers cannot be tested on tweets, because the medium itself halves clause density.

**The layers do not line up.** The linguistic literature locates new-speaker differences mainly in phonology and syntactic complexity in speech. The computational literature measures spelling and vocabulary in writing. Until the same speakers are observed in both, each field is describing a different object.

**Generation changes the question.** Tools that check spelling push writers toward the norm. Tools that generate text supply a model of the language, and the quality of that model depends on training data whose provenance has not been audited. Whether model-produced Irish is feeding back into school Irish is an open empirical question.

# 6. Limitations

- The tweets date from 2009 to 2019 and come from one platform. Much current informal use is on video and private messaging services, for which no corpus exists. Section 7 describes a tool for extending the series, which has not yet been run.
- Counts remain modest: 37 cases of unwritten lenition and 4 of unwritten eclipsis in tweets.
- The learned contexts cover lenition and eclipsis of consonants after a preceding word or word pair. Prefixed *h*, *t* and *n-* before vowels, and mutations triggered by gender or case with no adjacent trigger, are not covered.
- The contexts assume the written standard as reflected in one treebank.
- The word lists are short and have not been independently reviewed.
- The two tweet sub-corpora overlap in time and differ in sampling and annotation.
- Online samples over-represent adult, urban and institutional accounts and include bots and machine translation.
- The literature search ran in English-language indexes and will have missed work published in Irish.
- Several sources were read only in part, as marked.

# 7. Extending the data, and the risks of doing so

No openly available collection of Irish tweets after 2019 was found. Free research access to the platform has ended, and reading posts through the official interface is now charged per post (about $0.005 at the time of writing, with full-archive search requiring a higher access level). The repository therefore includes a collector, `scripts/collect_posts.py`, that the author can run with their own credentials against the official X interface or the Bluesky interface. It has been tested only on constructed data and has not been run against either live service.

The collector is built so that the risks of handling public posts are reduced by design.

| Risk | Control |
|---|---|
| Re-identifying writers in a small language community | Text, post identifiers and account names are held in memory only. The sole output is a table of yearly totals, and a year with fewer than 200 Irish posts is suppressed |
| Personal data in posts | Mentions, links and hashtags are stripped before analysis |
| Breaching platform terms | Official interfaces only, with the author's own credentials. No scraping |
| Unplanned cost | A cost estimate is printed and nothing is requested without an explicit flag |
| Leaked credentials | Read from environment variables, never from files or command arguments |
| Non-Irish posts inflating the counts | A second language check, since platform language tags for Irish are unreliable |
| Writers' backgrounds and ages are unknown | No claim is made about who wrote any text, and results are reported for texts only |
| Over-reading small numbers | Intervals are reported, and the eclipsis claim was withdrawn when wider data did not support it |
| Unverified sources | References not read in full are marked, and several were checked and corrected in this version |

No new data was collected from people for this paper and no platform was scraped. Only aggregate statistics are reported, and the example sentences in the repository are constructed. The feature extractor is documented as unsuitable for profiling individuals or grading writing. Any study in schools would need institutional ethics approval, the consent arrangements that such research requires, and agreement with the schools and their patron bodies. The full risk register is in `docs/risks.md`.

# 8. Research agenda

The repository's gap register lists eighteen gaps. Five matter most.

1. **Model errors against learner errors.** Compare the grammatical categories on which language models fail (Irish-BLiMP) with those on which learners fail (the pupil corpus and the learner corpus). This needs no new human data.
2. **Training-data audit.** Sample the sources used to train Irish models and have fluent raters estimate the share that is machine-translated or non-fluent.
3. **Speaker background.** Collect donated digital writing with a short background questionnaire, so that school type and home language are known.
4. **Phonology.** Measure the palatalisation contrast acoustically in learner recordings that speech projects already hold, with consent.
5. **Generative AI in Irish-medium classrooms.** A government advisory paper warns of a divide for Gaelscoileanna (AI Advisory Council 2025), and no study has observed what pupils and teachers do.

# 9. Conclusion

Computational methods can already show, cheaply and reproducibly, how far a piece of Irish sits from the written standard and how that distance differs across registers and samples. They cannot yet say who wrote it or why. Closing that gap is a matter of consented data with speaker background, and of bringing the classroom literature and the corpus literature onto the same speakers.

# References

† = identified from an abstract or repository record and not read in full.

- AI Advisory Council (2025). *AI and Education*. Government of Ireland advice paper, February 2025. <https://enterprise.gov.ie/en/publications/publication-files/ai-advisory-council-ai-on-education-paper.pdf>
- Barry, J. et al. (2022). gaBERT: an Irish language model. *LREC 2022*. <https://arxiv.org/abs/2107.12930>
- Cassidy, L., Lynn, T., Barry, J. and Foster, J. (2022). TwittIrish: a Universal Dependencies treebank of tweets in modern Irish. *ACL 2022*. <https://aclanthology.org/2022.acl-long.473/>
- Caulfield, J. (2013). *A social network analysis of Irish language use in social media*. PhD thesis, Cardiff University. † <https://orca.cardiff.ac.uk/53228/>
- CSO (2023). Census of Population 2022, Summary Results: Education and Irish Language. <https://www.cso.ie/en/releasesandpublications/ep/p-cpsr/censusofpopulation2022-summaryresults/educationandirishlanguage>
- Hickey, T. M. (2009). Code-switching and borrowing in Irish. *Journal of Sociolinguistics* 13, 670-688. † <http://hdl.handle.net/10197/4792>
- IRLBench (2025). IRLBench: a multi-modal, culturally grounded, parallel Irish-English benchmark for open-ended LLM reasoning evaluation. arXiv:2505.13498. (Cited by title; author list not confirmed.) <https://arxiv.org/abs/2505.13498>
- Kilgarriff, A., Rundell, M. and Uí Dhonnchadha, E. (2006). Efficient corpus development for lexicography: building the New Corpus for Ireland. *Language Resources and Evaluation* 40. †
- Lynn, T. and Scannell, K. (2019). Code-switching in Irish tweets: a preliminary analysis. *Celtic Language Technology Workshop*, 32-40. <https://aclanthology.org/W19-6905/>
- McGiff, J. et al. (2025). Irish-BLiMP: a linguistic benchmark for evaluating human and language model performance in a low-resource setting. <https://arxiv.org/abs/2510.20957>
- McInerney, J. et al. (2026). Qomhrá: a bilingual Irish and English large language model. *LoResLM 2026*. <https://arxiv.org/abs/2510.17652>
- Ní Chiaráin, N. et al. (2022). An Corpas Cliste: creating a learner corpus for Irish from a new, purpose-built iCALL platform. *EUROCALL 2022*. <https://files.eric.ed.gov/fulltext/ED625169.pdf>
- Nic Fhlannchadha, S. and Hickey, T. M. (2021). Where are the goalposts? Generational change in the use of grammatical gender in Irish. *Languages* 6(1), 33. <https://doi.org/10.3390/languages6010033>
- Nic Leoid, N. (2023). *Structure and functions of Irish-English codeswitching as used by young Conamara Gaeltacht speakers*. PhD thesis, University of Edinburgh. † <https://era.ed.ac.uk/handle/1842/41059>
- Ó Broin, B. (2010). Schism fears for Gaeilgeoirí. *Irish Times*, 16 January 2010. <https://www.irishtimes.com/life-and-style/people/schism-fears-for-gaeilgeoiri-1.1269494>
- Ó Duibhir, P. (2009). *The spoken Irish of sixth-class pupils in Irish immersion schools*. PhD thesis, Trinity College Dublin. † <https://edepositireland.ie/handle/2262/78131>
- Ó Duibhir, P. and Garland, J. (2010). *Gaeilge labhartha na bpáistí i scoileanna lán-Ghaeilge i dTuaisceart na hÉireann / The spoken Irish of pupils in Irish-medium schools in Northern Ireland*. SCoTENS, December 2010. (Read in part.) <https://scotens.org/docs/spokenirish.pdf>
- Ó Duibhir, P., Ní Dhiorbháin, A. and Cosgrove, J. (2016). An inductive approach to grammar teaching in Grade 5 and 6 Irish immersion classes. *Journal of Immersion and Content-Based Language Education* 4(1). †
- Ó Meachair, M. J. et al. (2026). Corpas Náisiúnta na Gaeilge 2022-2029: a project overview. *CMLC 2026*, 63-65. <https://aclanthology.org/2026.cmlc-1.8/>
- O'Rourke, B. and Walsh, J. (2015). New speakers of Irish: shifting boundaries across time and space. *International Journal of the Sociology of Language* 231, 63-83. <https://doi.org/10.1515/ijsl-2014-0032>
- Péterváry, T., Ó Curnáin, B., Ó Giollagáin, C. and Sheahan, J. (2014). *Analysis of Bilingual Competence: Language Acquisition among Young People in the Gaeltacht*. COGG. †
- Scannell, K. (n.d.). Slides on minority languages, Wikipedia quality and LLM training data. <https://docs.google.com/presentation/d/13rAl4f5BiholQ3P-AF1PWTwMNSxTW9a8/htmlpresent>
- Snesareva, M. (2017). Palatalisation in Dublin Irish, or how to speak Irish with a Dublin accent. *Studia Celtica Posnaniensia* 2(1), 63-80. <https://doi.org/10.1515/scp-2017-0004>
- Snesareva, M. (2018). Drifting towards ambiguity: a closer look at palatalisation in L2 Irish. *Studia Celto-Slavica* 8, 55-69. <https://ulster.ac.uk/celtoslavica/series/08/07>
- The Journal (2025). Most of the Irish-language Wikipedia was written by editors who did not speak Irish. <https://thejournal.ie/gaeilge-wikipedia-written-by-editors-who-did-not-speak-irish-6589572-Jan2025/>
- Tran, K.-T., O'Sullivan, B. and Nguyen, H. D. (2024). UCCIX: Irish-eXcellence large language model. *ECAI 2024*. <https://arxiv.org/abs/2405.13010>
- Walsh, J., O'Rourke, B. and Rowland, H. (2015). *Research Report on New Speakers of Irish*. Foras na Gaeilge. †
