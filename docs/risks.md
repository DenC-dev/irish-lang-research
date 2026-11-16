# Risk register

*Version 0.4, 16 November 2026.* Each row says what could go wrong, what has been done, and what is still open.

## Data and privacy

| Risk | What has been done | Still open |
|---|---|---|
| A writer is re-identified from style or dialect in a small language community | Scripts write totals only. The collector holds text, post identifiers and account names in memory and suppresses any year with fewer than 200 Irish posts | None for published outputs. Anyone who modifies the collector to save text takes on this risk |
| Personal data inside posts | Mentions, links and hashtags are stripped before analysis. The treebank maintainers had already anonymised usernames, phone numbers and emails | Names inside running text are still processed in memory |
| The ages and backgrounds of writers are unknown | No claim is made about who wrote any text. Results describe texts | Cannot be fixed without consented background data |
| Breaching platform terms | Official interfaces only, with the owner's own credentials. No scraping | The owner must check current developer terms and university rules before running the collector |
| Unplanned spending on the X interface | The collector prints an estimate (about $70 for 2,000 posts a year over 2020 to 2026 at the reported $0.005 a read) and does nothing without `--yes-spend` | Prices change. Full-archive search may need a higher access level |
| Leaked credentials | Read from environment variables only | Keep them out of shell history and out of the repository |
| Licence breach | The treebanks (CC BY-SA 3.0 and 4.0) are downloaded by script and not redistributed | None known |

## Method

| Risk | What has been done | Still open |
|---|---|---|
| Hand-picked rules miss cases or mislead | `mutation_contexts.py` learns every context where edited text mutates at least 95% of the time on at least 20 occasions (18 for lenition, 14 for eclipsis) and tests on held-out text | Vowel-initial mutations (*h*, *t*, *n-*) and mutations with no adjacent trigger are not covered |
| A dialect form counted as an error | Outcomes are split three ways, so lenition where the standard eclipses is reported separately | The contexts still reflect one treebank's version of the standard |
| An earlier claim was wrong | The eclipsis gap (5.0% against 0.2%) did not survive the wider analysis (0.9% against 0.0%) and has been withdrawn in the paper, the site and the README | None |
| Small counts over-read | Wilson intervals throughout. The lenition result now rests on 37 cases in 388 contexts, up from 18 in 177 | Eclipsis and the between-sample lenition change are too small to call |
| Too many comparisons | p-values are flagged as uncorrected, with the Bonferroni threshold stated | No correction is applied to the headline tables |
| Tokens in one tweet are not independent | Stated wherever a test is reported | A tweet-level bootstrap would be the proper fix |
| The two tweet samples were annotated differently | Annotation-independent measures (length marks) are separated from annotation-dependent ones | Cannot be resolved without re-annotation |
| Bots and machine translation in the tweets | Noted as a limit | Not filtered |
| Platform language tags for Irish are unreliable | The collector applies a second check using common Irish words | The check will drop very short posts and some heavily mixed ones |
| The collector has never met a live service | Tested with constructed responses for paging, filtering and output | Endpoint details may need adjusting on first real run |
| Results cannot be reproduced | Treebank commits are pinned, scripts are deterministic, and the standard library is the only dependency | None known |

## Sources

| Risk | What has been done | Still open |
|---|---|---|
| A reference is wrong | Five uncertain entries were checked and corrected in this version: Ó Duibhir and Garland (2010), Ó Murchadha and Kavanagh (2022), Ó Béarra (2007), Ó Broin (2010) and Antonijevic, Durham and Ní Chonghaile (2017) | Three are still unconfirmed: the author list of IRLBench, the co-authors of Dereza et al. (2023), and the author and title of the CLTW 2025 paper cited as Ward (2025) |
| A source was read only in part | Marked † in each reference list | Read in full before quoting |
| Work published in Irish was missed | Stated as a limit | A search pass in Irish |
| News and blog sources carry weight they should not | Labelled as anecdotal or as press reports where used | The Duolingo voice claims and some school counts rest on such sources |

## Use and presentation

| Risk | What has been done | Still open |
|---|---|---|
| The rules are used to grade writing or label people | The README, the site and the ethics file say they are unsuitable for that. The site demo words its output as what "the standard writes" | Cannot be prevented in an open repository |
| Deficit framing of new speakers | "Error" is avoided for the project's own measures, and the choice of the standard as reference point is stated | The cited classroom literature uses error counts |
| Readers take this for peer-reviewed work | The paper and site state that it has not been peer reviewed | None |
| AI assistance not disclosed | Disclosed in the paper and on the site | Check the wording against the rules of any venue or course before submitting |
| Example sentences or word lists contain mistakes | The author speaks Irish | Independent review by a second speaker has not happened yet |
