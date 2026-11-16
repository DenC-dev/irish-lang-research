# Contemporary Irish, Gaelscoileanna and the Internet: A Computational-Linguistics Overview

*Version 0.4, 16 November 2026. Literature located by web search on that date; see section 10 for what that search could and could not cover. Continued in [`evolution.md`](evolution.md) (how the language, schools, technology and research have changed) and [`gaps.md`](gaps.md) (full gap register).*

## How to read the evidence labels

Claims are tagged so that their status stays visible:

- **[E] Established**: reported in a peer-reviewed study, official statistics, or a published resource paper. "Established" describes the source, and many of these studies are small.
- **[P] Pilot**: a number computed in this repository from public treebanks (section 7). Descriptive only.
- **[H] Hypothesis**: a plausible claim that I could not find tested.
- **[A] Anecdotal**: journalism, blogs, or community observation.

## 1. Scope

This overview asks what computational linguistics can currently say about two overlapping things: the Irish acquired and used in Irish-medium schools outside the Gaeltacht (Gaelscoileanna at primary level, Gaelcholáistí at post-primary), and the Irish written in digital communication. The two are usually studied apart. Immersion Irish is studied by applied linguists with classroom recordings and tests, while online Irish is studied by NLP researchers with tweets. Nobody, as far as I could find, has joined the two with data (section 10).

## 2. Who uses Irish, and where

- **[E]** In Census 2022, 623,961 people reported speaking Irish daily when use inside the education system is included, while 71,968 reported daily use outside education, 1,835 fewer than in 2016 (CSO 2023a).
- **[E]** The same census asked about ability for the first time: over four in ten Irish speakers said they spoke it well or very well, and 55% said they could not speak it well (CSO 2023b).
- **[E]** Irish-medium schooling outside the Gaeltacht is a substantial sector. A 2015/16 count gives 144 immersion primaries with 35,850 pupils and 42 post-primary schools with 11,008 (Hickey 2016). Those figures are a decade old and should be refreshed from Gaeloideachas before reuse.

The gap between "daily within education" and "daily outside education" is the basic fact behind everything below. For most young users, school is where Irish happens, so any corpus of young people's Irish is to a large degree a corpus of school-shaped Irish.

## 3. What "contemporary", "new" or "learner-influenced" Irish means

Four labels circulate and they are not synonyms.

| Term | What it picks out | Status |
|---|---|---|
| **Traditional / Gaeltacht Irish** | Home-acquired Irish in the Ulster, Connacht and Munster dialect areas | Descriptive category; itself changing (below) |
| **An Caighdeán Oifigiúil** | The written standard introduced in the mid twentieth century (Scannell 2014) | A written norm with no native speech community of its own |
| **New speakers** | People who use Irish regularly without being traditional native speakers; defined broadly because speaker types vary so much (Walsh, O'Rourke and Rowland 2015) | Sociolinguistic category about people |
| **"Gaelscoilis", "post-Gaeltacht Irish"** | Labels for the speech of immersion pupils and urban new speakers. Ó Duibhir (2012) reports "Gaelscoilis" alongside the dismissive *Gaeilge líofa lofa* ("rotten fluent Irish") | Folk and scholarly labels about varieties; partly evaluative |

Three cautions follow from the literature.

**There is no single Gaelscoil variety. [E]** In the one sizeable spoken corpus, the share of utterances containing an error ranged from 20.5% to 41.6% across the all-Irish schools sampled, and pupils in Northern Ireland used Ulster forms such as *thig* more than pupils in the Republic (Ó Duibhir and Garland 2010). Schools differ in intake, teacher dialect, region and age profile. A feature list describes tendencies in samples, and treating it as the grammar of a dialect goes beyond the evidence.

**Native-speaker Irish is not a fixed benchmark. [E]** Nic Fhlannchadha and Hickey (2021) tested 135 proficient adults and 306 young speakers aged 6 to 13 in Gaeltacht communities on grammatical gender and concluded that young speakers there are exposed to considerable variability in the adult input. Péterváry et al. (2014) recorded 50 Conamara pupils aged 7 to 12 from Irish-only homes and found their English outstripping their Irish. Gaeltacht schools also enrol pupils with very different home exposure (Antonijevic, Durham and Ní Chonghaile 2017). A learner/native contrast therefore cannot be drawn by school type or postcode.

**The labels carry ideology. [E]** In a matched-sample experiment, teachers rated traditional Gaeltacht speech significantly more positively than post-Gaeltacht speech when asked directly (Ó Murchadha and Kavanagh 2022). O'Rourke and Walsh (2015) show that idealising the traditional speaker can undermine new speakers' sense of legitimacy. Any tool that scores text as "learner-like" inherits this politics.

## 4. What is documented about school-acquired Irish

The core dataset is Ó Duibhir's corpus of pupil talk during a collaborative task, extended in a cross-border study (Ó Duibhir 2009; Ó Duibhir and Garland 2010; synthesised in Ó Duibhir 2018). **[E]** throughout:

| Group | Pupils | Words transcribed | Utterances with an error | English words |
|---|---:|---:|---:|---:|
| Irish-medium, Northern Ireland | 24 | 14,394 | 32.1% | 8.75% |
| All-Irish, Republic | 65 | 30,783 | 29.2% | 10.03% |
| Gaeltacht | 15 | 4,557 | 2.6% | 6.65% |

- **Syntax is mostly target-like where Irish and English differ most visibly.** Verb-subject-object and noun-adjective order were used correctly.
- **The persistent non-target features are the copula (*is*) versus the substantive verb (*bí*) and verbal-noun clauses**, with pupils mapping English structure onto Irish.
- **Most English material is a small set of discourse markers.** Eight items (*so, right, yeah, no, just, like, then, okay*) made up the majority of English tokens in all three groups, including the Gaeltacht group. This is a shared bilingual practice, and it does not separate learners from native speakers.
- **The school norm targets language choice more than accuracy.** All 11 peer-correction episodes corrected the use of English, and none corrected an Irish form.
- **Explicit teaching moves accuracy.** An explicit-inductive intervention on the genitive with 274 pupils in 12 classes produced a significant gain that levelled off at delayed post-test (Ó Duibhir, Ní Dhiorbháin and Cosgrove 2016; Ní Dhiorbháin and Ó Duibhir 2017). A corrective-feedback study found the same errors recurring in two fifth and sixth classes (Ní Mhurchú, Ní Aogáin and Ó Ceallaigh 2023).

Limits the authors state themselves: observer effects, a single meaning-focused task, 20 minutes per group, a small Gaeltacht group that included in-migrant families, and few raters. The corpus is also about fifteen years old and is speech, so it says nothing direct about how these pupils write or type.

## 5. Irish in digital communication

### Who is online

- **[E]** Caulfield (2013) audited the Irish-language blogosphere, Twittersphere and a Facebook group and found networks of roughly 150 to 300 regular participants each, mostly adult, male and urban outside the Gaeltacht.
- **[E]** A survey of 617 Irish users found social and technical factors jointly shaping whether people use the language on social media (Lackaff and Moner 2016).
- **[A]** Journalism from 2025 describes a "#GaelTok" scene and tens of thousands of posts tagged #Gaeilge (Irish Post 2025). I found no peer-reviewed linguistic analysis of Irish on TikTok, Instagram, Snapchat, WhatsApp or Discord.

### Vocabulary and contact

- **[E]** In 1,496 annotated tweets, 254 (16%) contained code-switching. Of 943 English tokens, about 43% were inter-sentential, 26% were bilingual restatements of the same content, and 31% were intra-sentential (Lynn and Scannell 2019).
- **[E]** Word-internal mixing was rare in that sample (two tokens, *an-talent* and *an-time*), which the authors say conflicts with their intuition from speech.
- **[E]** Attested hybrid forms include English nouns under Irish noun-adjective order (*podcast úr*) and Gaelicised spellings (*stuif*, *albam*). The authors leave the borrowing/switching boundary open.
- **[E]** Only 38.32% of the unique lemmas in the TwittIrish treebank occur in the training portion of the standard-text treebank, so tweet vocabulary is largely unseen by tools trained on edited prose (Cassidy et al. 2022).

### Spelling

- **[E]** About 2.5% of TwittIrish tokens show orthographic variation: omitted length marks (*síneadh fada*), abbreviation, letter lengthening, phonetic respelling of English (*fair plé*) and typos (Cassidy et al. 2022).
- **[E]** Initialisms such as GRMA (*go raibh maith agat*, "thank you") are attested in the treebank. **[A]** Longer lists (for example NASAA for *níl ach saol amháin agat*) come from blogs and learner diaries (Notre Dame SLA blog 2016) and have no frequency evidence behind them.
- **[E]** Irish orthography is more regular than English yet still hard for beginning readers whose first literacy is English (Stenson and Hickey 2016). **[H]** Fada omission online probably mixes keyboard friction with uncertainty about the spelling, and the two cannot be told apart from text alone.

### Grammar and register

- **[E]** Tweets show contractions (*gowil* for *go bhfuil*), dropped copulas, dialect forms (*domh*), variation between synthetic and analytic verb forms, and hashtags or @-mentions filling syntactic roles (Cassidy et al. 2022).
- **[E]** The treebank authors note that second-language users can produce unintended deviations and that some tweets look machine-translated or bot-written. They report no first-language/second-language breakdown, because the data do not contain one.

That last point matters most for this overview. Online corpora record text, and speaker background is not recoverable from text without consent-based metadata.

## 6. Methods and resources, and what each can reveal

| Resource or method | What exists | What it can show | Main limitation or bias |
|---|---|---|---|
| **Reference corpora** | New Corpus for Ireland, c. 30m words (Kilgarriff et al. 2006); Corpus of Contemporary Irish, 14.9m (Ní Loingsigh et al. 2017); Corpas Náisiúnta na Gaeilge, 101m words in phase 1, with a 6.5m-word spoken corpus planned and work running to 2029 (Ó Meachair et al. 2022, 2026) | Frequencies, variant forms, change over time in published writing | Published and edited text; school-age and informal digital writing largely absent |
| **Treebanks** | UD Irish-IDT (news, fiction, web, legal, government); UD TwittIrish, 2,596 tweets | Quantified differences between edited and user-generated Irish | Tweets from 2009 to 2019; adults; one annotator for most of TwittIrish |
| **Learner corpora** | TEG exam corpus, 150,000 to 200,000 words at B1 to C1 (Digital Plan 2022); An Corpas Cliste from the *An Scéalaí* platform, 44,093 stories and 5.7m words from second- and third-level learners (Ní Chiaráin et al. 2022); a Maynooth error-annotated corpus in development with COGG support (Maynooth University n.d.) | Error profiles by level; keystroke-level revision behaviour | Adult or exam settings; school type not reported; published paper gives no consent or anonymisation detail; automatic and manual error counts disagreed sharply |
| **Spelling and grammar tools** | GaelSpell and An Gramadóir (Scannell); neural mutation prediction (Scannell 2020); orthographic standardisers (Scannell 2014; Ó Raghallaigh, Scannell and Dowling 2019) | Scalable candidate detection of non-standard forms | Built around the Caighdeán, so legitimate dialect forms are flagged; An Gramadóir was judged unfit for learner feedback in the Corpas Cliste study |
| **Language models** | gaBERT, 7.9m sentences (Barry et al. 2022); UCCIX on Llama 2 (Tran et al. 2024); Qomhrá (McInerney et al. 2026) | Parsing gains (+10 LAS on tweets); surprisal or probing as a measure of distance from the standard | Training text is web crawl, Wikipedia, parallel and official text; Qomhrá's instruction data is LLM-translated |
| **Model evaluation** | Irish-BLiMP, 1,020 minimal pairs: humans 90.1%, best model 73.5% (McGiff et al. 2025); IRLBench from Leaving Certificate papers (2025) | Which grammatical contrasts models do and do not control | Standard grammar only; fluent human raters; no dialect or informal items |
| **Machine translation** | English-Irish NMT with human evaluation (Dowling 2022; Lankford, Afli and Way 2024) | Error typologies by fluency and accuracy | Training data dominated by public-administration translation |
| **Speech** | ABAIR synthesis and recognition; Fotheidil transcription (Lonergan et al. 2022, 2023, 2024) | Dialect identification and dialect-wise error rates | Accuracy uneven across dialects even with balanced data; very little speech data from young speakers (Ulster University n.d.) |

Three method-level observations.

1. **Parsers measure distance from the standard, and that is all they measure. [E]** Systems trained on edited text lose 23 to 25 labelled-attachment points on tweets (Cassidy et al. 2022). The drop is a useful index of how far a text sits from the training register, but it conflates dialect, informality, code-switching, typing and learner forms.
2. **Language models are standard-biased by construction. [E/H]** The composition of gaBERT's and UCCIX's training data is documented. That the resulting models underrate or "correct" dialectal and new-speaker forms is a reasonable inference **[H]** that Irish-BLiMP does not test, since its items come from grammar reference works.
3. **Synthetic data creates a feedback loop. [H]** Qomhrá's authors state that their data quality is bounded by the Irish that closed LLMs produce and that evaluation relied on one native speaker and one learner. If pupils then draft with such systems, model Irish becomes input to school Irish. I found no study of AI-assisted writing in Irish-medium schools.

## 7. Pilot analysis in this repository [P]

To make the edited/online contrast concrete with open data, `scripts/compare_treebanks.py` runs the same surface measures over UD Irish-IDT and UD TwittIrish and summarises TwittIrish's token-level annotations. Full output is in `results/treebank_comparison.md`.

| Measure | Edited (IDT) | Tweets (TwittIrish) |
|---|---:|---:|
| Mean tokens per sentence or tweet | 23.6 | 18.4 |
| Words carrying a fada | 31.8% | 26.3% |
| Missing-fada candidates per 1,000 words (30-word list) | 0.04 | 3.37 |
| English function words per 1,000 words (list-based lower bound) | 0.68 | 11.73 |
| Eight English discourse markers per 1,000 words | 0.30 | 0.84 |
| *mo/do* + lenitable common noun written without lenition | 3 of 474 (0.6%) | 18 of 177 (10.2%, 95% CI 6.5 to 15.5) |
| *ár/bhur/i* + eclipsable common noun written without eclipsis | 2 of 881 (0.2%) | 7 of 139 (5.0%, 95% CI 2.5 to 10.0) |

From TwittIrish's own annotation: 5.9% of language-tagged tokens are English, 22.3% of tweets contain at least one English token, and 923 tokens carry a corrected form (23.5 per 1,000 words), of which about 41% differ from the written form only in diacritics.

How to read this:

- The figures agree with the published ones (about a quarter of tweets multilingual; 2.5% orthographic variation), which is a sanity check on the code more than a new finding.
- The mutation contrast is the new piece. In IDT, 471 of 474 lenition contexts are lenited, so the rule itself is sound on standard text.
- **Superseded for mutation (version 0.4).** `scripts/mutation_contexts.py` replaces the hand-picked triggers with every context the edited treebank supports. Lenition holds up: unwritten in 9.5% of tweet contexts (37 of 388) against 1.2% in held-out edited text. Eclipsis does not: 0.9% (4 of 424) against 0.0%. The 5.0% eclipsis figure in the table above included lenited forms that are legitimate in some dialects and should be set aside. See `results/mutation_contexts.md`.
- **The contrast does not show that tweeters are learners.** Unmarked mutation can reflect fast typing, autocorrect, English or brand-name nouns (3 of the 25 cases), dialect, or deliberate informality. The counts are small, the tweets predate 2020, and the eclipsis rule for *i* ignores some legitimate patterns.
- The discourse markers that dominate pupils' speech are rare in tweets. That fits a speech/writing difference, although the comparison is across studies with different methods.

## 8. Limitations and biases across the field

- **Platform and period bias.** Almost all quantified evidence on online Irish comes from Twitter between 2006 and 2019. Young people's use has since moved to video and private messaging, where no corpus exists.
- **Who is counted.** Online samples over-represent adult, urban, new-speaker and institutional accounts (Caulfield 2013), and include bots and machine translation.
- **Standard-language bias.** Taggers, checkers, benchmarks and model training data are anchored to the Caighdeán. Dialect is thinly marked even in gold data: only 120 IDT tokens carry a dialect tag **[P]**.
- **Translationese.** Much written Irish in model training sets is translated from English for official purposes (Dowling 2022; Lynn 2023), which is itself a contact variety and is rarely discussed as one.
- **Deficit framing.** "Error rate" presupposes a target. Given the variability in adult Gaeltacht input, the choice of target is a research decision that should be stated.
- **Annotation scarcity.** Single annotators, moderate agreement on switch types (kappa 0.69 to 0.74), and evaluations resting on one or two speakers are common.
- **Speech and text are different objects.** The school evidence is spoken and the online evidence is written, so cross-comparison is indirect.

## 9. Gaps

### School-age language

- No open corpus of pupils' written or typed Irish exists. The largest public body of school writing is the 1930s Schools' Collection (Ward 2025), which is a historical source.
- The spoken immersion corpus is small, dated and not public.
- No longitudinal data follow the same pupils from primary through post-primary or into adult use.
- Speech data from young speakers is very small. One first-language acquisition corpus follows a single Gaeltacht family (Cameron-Faulkner and Hickey 2011), and a new project is recording speech in the home for speech recognition (Ulster University n.d.). Nothing comparable exists for immersion pupils. (Corrected in version 0.2; see `gaps.md`.)

### Privacy and ethics

- Personal data fall under GDPR, with stricter rules for under-18s, and Ireland sets the digital age of consent at 16. Platforms set minimum ages, so the online writing of school-age users is largely private or out of scope by design.
- **[H, my inference]** Re-identification risk is unusually high. With active public networks numbering in the hundreds, dialect, school and writing habits can identify a person even after usernames are removed. TwittIrish anonymised usernames, phone numbers and emails in 2023, which addresses direct identifiers only.
- Platform access has tightened since 2023, so the existing tweet corpora are hard to extend or replicate.
- The practical route is consent-based collection inside schools with guardians' permission, data donation, aggregate-only release, and governance shared with Irish-medium education bodies. This repository therefore ships constructed examples and aggregate statistics only (`ETHICS.md`).

### Under-representation of Irish online

- **[E]** Irish LLM work proceeds with hundreds of millions of tokens where comparable efforts for other languages used billions (Tran et al. 2024). The European Language Equality report classed machine translation support for Irish as fragmentary and listed missing technologies (Lynn 2023). A Digital Plan for the Irish Language was published in December 2022.
- Scarcity has a second-order effect. Whatever text is available becomes the model's Irish, so the register mix of the web is amplified.

### Unanswered questions

1. Do features documented in immersion speech (copula/*bí*, verbal-noun clauses, unmarked mutation) appear at different rates in the digital writing of former immersion pupils, Gaeltacht-raised writers and adult learners? This needs consented metadata.
2. Are online innovations (Gaelicised spellings, initialisms, hybrid intensifiers) spreading across speaker groups or confined to small networks?
3. Do predictive keyboards, spellcheckers and LLM assistants shift users toward the Caighdeán and away from dialect forms?
4. How do Irish LLMs and grammar tools score matched standard, dialectal and new-speaker sentences?
5. What do teachers and pupils in Irish-medium schools actually do with machine translation and chatbots?

## 10. Is there already a paper on this?

Short answer: I found adjacent work on each side and nothing that joins them.

| Closest existing work | Covers | Does not cover |
|---|---|---|
| Ó Duibhir (2009, 2018); Ó Duibhir and Garland (2010) | Corpus of immersion pupils' speech | Digital writing; computational methods beyond frequency lists |
| Cassidy et al. (2022); Cassidy (2024); Lynn and Scannell (2019) | Computational analysis of Irish tweets, including contact phenomena | Speaker background; school-acquired Irish; anyone under 18 |
| Ní Chiaráin et al. (2022) | Learner corpus harvested from a digital platform | Immersion pupils as a group; informal communication |
| Caulfield (2013) | Who uses Irish on social media and how they adapt it | Computational linguistic analysis; schools |
| McGiff et al. (2025); Tran et al. (2024); McInerney et al. (2026) | Irish LLMs and their grammatical evaluation | Variation, learners, or informal registers |

So a study that links immersion-acquired Irish to digital writing using computational methods appears to be open ground, and the pilot in section 7 is, to my knowledge, not duplicated elsewhere. Three caveats on that claim: the search was in English-language indexes and would miss work published in Irish (for example in *Léann Teangeolaíochta* or *COMHARTaighde*) and unpublished theses; Cassidy's 2024 thesis treats language contact in tweets at length and should be read in full before any novelty claim goes into print; and the Maynooth learner-corpus project may release relevant data.

## 11. Summary of evidence status

| Claim | Status |
|---|---|
| Immersion pupils reach fluent, communicatively effective Irish with persistent non-target features in specific areas | E |
| Those features vary by school and region | E (one study) |
| The Irish of young Gaeltacht speakers is also changing under contact | E |
| Irish tweets differ measurably from edited Irish in spelling, lexis and syntax | E, replicated here (P) |
| Unmarked mutation is far more frequent in tweets than in edited text | P |
| Online non-standard features are driven by school-acquired Irish | H, untested |
| Digital tools are standardising young people's Irish | H, untested |
| LLM-generated Irish is feeding back into learners' Irish | H, untested |
| Text-speak initialisms beyond GRMA are in common use | A |
| Irish is flourishing among teenagers on TikTok | A |

## Bibliography

Entries marked † were identified from repository or publisher records during this search but not opened in full; check details against the original before citing.

- Antonijevic, S., Durham, R. and Ní Chonghaile, Í. (2017). Language performance of sequential bilinguals on an Irish and English sentence repetition task. *Linguistic Approaches to Bilingualism* 7(3-4), 359-393. † <https://doi.org/10.1075/lab.15026.ant>
- Barry, J., Wagner, J., Cassidy, L., Cowap, A., Lynn, T., Walsh, A., Ó Meachair, M. J. and Foster, J. (2022). gaBERT: an Irish language model. *LREC 2022*. <https://arxiv.org/abs/2107.12930>
- Cassidy, L. (2024). *Linguistic analysis and automatic dependency parsing of tweets in modern Irish*. PhD thesis, Dublin City University. † <https://doras.dcu.ie/29326/>
- Cassidy, L., Lynn, T., Barry, J. and Foster, J. (2022). TwittIrish: a Universal Dependencies treebank of tweets in modern Irish. *ACL 2022*. <https://aclanthology.org/2022.acl-long.473/>
- Caulfield, J. (2013). *A social network analysis of Irish language use in social media*. PhD thesis, Cardiff University. † <https://orca.cardiff.ac.uk/53228/>
- CSO (2023a). Census of Population 2022, Summary Results: Education and Irish Language. <https://www.cso.ie/en/releasesandpublications/ep/p-cpsr/censusofpopulation2022-summaryresults/educationandirishlanguage>
- CSO (2023b). Census of Population 2022, Profile 8: The Irish Language and Education. <https://www.cso.ie/en/releasesandpublications/ep/p-cpp8/censusofpopulation2022profile8-theirishlanguageandeducation/keyfindings/>
- Department of Tourism, Culture, Arts, Gaeltacht, Sport and Media (2022). *Digital Plan for the Irish Language: Speech and Language Technologies 2023-2027*. (Source for the TEG learner corpus figure.) <https://assets.gov.ie/241755/e82c256a-6f47-4ddb-8ce6-ff81df208bb1.pdf>
- Dowling, M. (2022). *An investigation of English-Irish machine translation and associated resources*. PhD thesis, Dublin City University. † <https://doras.dcu.ie/26574>
- Hickey, T. M. (2016). Beyond the immersion revolution: meeting ongoing challenges. Plenary slides, 6th International Conference on Immersion Education. <https://mtgsked.com/pd/1350/download>
- Irish Post (2025). From Gaeltacht to TikTok: the rise of Irish language creators. (Journalism.) <https://www.irishpost.com/culture/from-gaeltacht-to-tiktok-the-rise-of-irish-language-creators-295814>
- Kilgarriff, A., Rundell, M. and Uí Dhonnchadha, E. (2006). Efficient corpus development for lexicography: building the New Corpus for Ireland. *Language Resources and Evaluation* 40. †
- Lackaff, D. and Moner, W. J. (2016). Local languages, global networks: mobile design for minority language users. *SIGDOC 2016*. † <https://dx.doi.org/10.1145/2987592.2987612>
- Lankford, S., Afli, H. and Way, A. (2024). Human evaluation of English-Irish Transformer-based NMT. <https://arxiv.org/abs/2403.02366>
- Lonergan, L., Qian, M., Berthelsen, H., Murphy, A., Wendler, C., Ní Chiaráin, N., Gobl, C. and Ní Chasaide, A. (2022). Automatic speech recognition for Irish: the ABAIR-ÉIST system. *CLTW 4*. <https://aclanthology.org/2022.cltw-1.7/>
- Lonergan, L., Qian, M., Ní Chiaráin, N., Gobl, C. and Ní Chasaide, A. (2023). Towards dialect-inclusive recognition in a low-resource language: are balanced corpora the answer? <https://arxiv.org/abs/2307.07295>
- Lonergan, L. et al. (2024). Fotheidil: an automatic transcription system for the Irish language. <https://arxiv.org/abs/2501.00509>
- Lynn, T. (2023). Language report Irish. In Rehm, G. and Way, A. (eds), *European Language Equality*. Springer. <https://doi.org/10.1007/978-3-031-28819-7_22>
- Lynn, T. and Scannell, K. (2019). Code-switching in Irish tweets: a preliminary analysis. *Celtic Language Technology Workshop 2019*, 32-40. <https://aclanthology.org/W19-6905/>
- Lynn, T., Scannell, K. and Maguire, E. (2015). Minority language Twitter: part-of-speech tagging and analysis of Irish tweets. *W-NUT 2015*. <https://aclanthology.org/W15-4301/>
- Maynooth University, Lárionad na Gaeilge (n.d.). Learner corpus research. Project page. <https://www.maynoothuniversity.ie/larionad-gaeilge-centre-irish-language/our-research>
- McGiff, J., Tran, K.-T., Mulcahy, W., Ó Luinín, D., Dalzell, J., Ní Bhroin, R., Burke, A., O'Sullivan, B., Nguyen, H. D. and Nikolov, N. S. (2025). Irish-BLiMP: a linguistic benchmark for evaluating human and language model performance in a low-resource setting. *LREC 2026* (arXiv:2510.20957). <https://arxiv.org/abs/2510.20957>
- McInerney, J., Tran, K.-T., Lonergan, L., Ní Chiaráin, N., Ní Chasaide, A. and Devereux, B. (2026). Qomhrá: a bilingual Irish and English large language model. *LoResLM 2026*. <https://arxiv.org/abs/2510.17652>
- Ní Chiaráin, N. et al. (2022). An Corpas Cliste: creating a learner corpus for Irish from a new, purpose-built iCALL platform. *EUROCALL 2022*. <https://files.eric.ed.gov/fulltext/ED625169.pdf>
- Ní Dhiorbháin, A. and Ó Duibhir, P. (2017). An explicit-inductive approach to grammar in Irish-medium immersion schools. *Language Awareness* 26(1), 3-24. †
- Ní Loingsigh, K., Ó Raghallaigh, B. and Ó Cleircín, G. (2017). The design and development of Corpas na Gaeilge Comhaimseartha. *Corpus Linguistics 2017*. † <https://www.birmingham.ac.uk/documents/college-artslaw/corpus/conference-archives/2017/general/paper58.pdf>
- Ní Mhurchú, C., Ní Aogáin, S. and Ó Ceallaigh, T. J. (2023). Aiseolas ceartaitheach mar réiteach ar easnaimh theangeolaíocha sa tumoideachas lán-Ghaeilge. *Teanga* 30, 81-108. † <https://journal.iraal.ie/index.php/teanga/article/view/5455>
- Nic Fhlannchadha, S. and Hickey, T. M. (2021). Where are the goalposts? Generational change in the use of grammatical gender in Irish. *Languages* 6(1), 33. <https://doi.org/10.3390/languages6010033>
- Notre Dame SLA blog (2016). Texting slang "as Gaeilge". (Learner blog.) <https://sites.nd.edu/sla2016/2016/07/20/texting-slang-as-gaeilge/>
- Ó Duibhir, P. (2009). *The spoken Irish of sixth-class pupils in Irish immersion schools*. PhD thesis, Trinity College Dublin. † <https://edepositireland.ie/handle/2262/78131>
- Ó Duibhir, P. (2012). An instructional experiment in grammar teaching in Irish immersion. Slides, Immersion 2012, CARLA. <https://archive.carla.umn.edu/conferences/past/immersion2012/handouts/ODuibhir_GrammarTeachinginIrish_Oct2012.pdf>
- Ó Duibhir, P. (2018). *Immersion Education: Lessons from a Minority Language Context*. Multilingual Matters. †
- Ó Duibhir, P. and Garland, J. (2010). *Gaeilge labhartha na bpáistí i scoileanna lán-Ghaeilge i dTuaisceart na hÉireann / The spoken Irish of pupils in Irish-medium schools in Northern Ireland*. SCoTENS, December 2010. (Read to roughly one third of the report.) <https://scotens.org/docs/spokenirish.pdf>
- Ó Duibhir, P., Ní Dhiorbháin, A. and Cosgrove, J. (2016). An inductive approach to grammar teaching in Grade 5 and 6 Irish immersion classes. *Journal of Immersion and Content-Based Language Education* 4(1). † <https://www.jbe-platform.com/content/journals/10.1075/jicb.4.1.02dui>
- Ó Meachair, M. J., Bhreathnach, Ú. and Ó Cleircín, G. (2022). Introducing the National Corpus of Irish project. *CLTW 4*, 99-103. <https://aclanthology.org/2022.cltw-1.14>
- Ó Meachair, M. J., Bhreathnach, Ú., Scannell, K., Měchura, M., Ó Raghallaigh, B. and Ó Cleircín, G. (2026). Corpas Náisiúnta na Gaeilge 2022-2029: a project overview. *CMLC 2026*, 63-65. <https://aclanthology.org/2026.cmlc-1.8/>
- Ó Murchadha, N. and Kavanagh, L. (2022). Language ideologies in a minority context: an experimental study of teachers' responses to variation in Irish. *Journal of Sociolinguistics* 26(2), 197-220. <https://www.tara.tcd.ie/bitstreams/ace6ec77-2744-486c-8a5b-0b6fd91e49b9/download>
- Ó Raghallaigh, B., Scannell, K. and Dowling, M. (2019). Improving full-text search results on dúchas.ie using language technology. *Celtic Language Technology Workshop 2019*. <https://aclanthology.org/W19-6909/>
- O'Rourke, B. and Walsh, J. (2015). New speakers of Irish: shifting boundaries across time and space. *International Journal of the Sociology of Language* 231, 63-83. <https://doi.org/10.1515/ijsl-2014-0032>
- O'Rourke, B. and Walsh, J. (2020). *New Speakers of Irish in the Global Context: New Revival?* Routledge. †
- Péterváry, T., Ó Curnáin, B., Ó Giollagáin, C. and Sheahan, J. (2014). *Analysis of Bilingual Competence: Language Acquisition among Young People in the Gaeltacht*. COGG. †
- Scannell, K. (2014). Statistical models for text normalization and machine translation. *Celtic Language Technology Workshop 2014*. <https://aclanthology.org/W14-4605/>
- Scannell, K. (2020). Neural models for predicting Celtic mutations. *SLTU-CCURL 2020*. <https://aclanthology.org/2020.sltu-1.1/>
- Stenson, N. and Hickey, T. M. (2016). When regular is not easy: cracking the code of Irish orthography. *Writing Systems Research* 8(2), 187-217. † <http://hdl.handle.net/10197/9049>
- Tran, K.-T., O'Sullivan, B. and Nguyen, H. D. (2024). UCCIX: Irish-eXcellence large language model. *ECAI 2024*. <https://arxiv.org/abs/2405.13010>
- Ulster University (n.d.). Automatic speech recognition models for children's language development. Project page. <https://pure.ulster.ac.uk/en/projects/automatic-speech-recognition-asr-models-for-childrens-language-de/>
- Walsh, J., O'Rourke, B. and Rowland, H. (2015). *Research Report on New Speakers of Irish*. Foras na Gaeilge. † <https://www.forasnagaeilge.ie/wp-content/uploads/2015/10/New-speakers-of-Irish-report.pdf>
- Ward, M. (2025). Paper on reusing existing Irish resources for game-based language learning, *CLTW 5*, 27-34. † (Author recalled, title not confirmed.) <https://aclanthology.org/2025.cltw-1.3.pdf>

**Data**

- UD Irish-IDT, commit `c30cbaa`, CC BY-SA 3.0. <https://github.com/UniversalDependencies/UD_Irish-IDT>
- UD Irish-TwittIrish, commit `a52a11b`, CC BY-SA 4.0. <https://github.com/UniversalDependencies/UD_Irish-TwittIrish>
