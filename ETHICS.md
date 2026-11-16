# Data rules for this project

1. **No data is collected in schools or from individual people, and none is stored or published here.** Example sentences are constructed.
2. **No scraping of social platforms.** The online-language data used is the published, licensed UD TwittIrish treebank, in which usernames, phone numbers and emails were anonymised by its maintainers. `scripts/collect_posts.py` can extend the series through official interfaces with the owner's own credentials. It keeps post text, identifiers and account names in memory only and writes yearly totals.
3. **Aggregate output only.** Scripts write counts and rates. They do not write tweet text.
4. **No profiling.** The feature extractor reports on texts. Do not aggregate its output by author, and do not use it to label a person as a learner, native speaker, or member of any group.
5. **Small-community risk.** Irish-language networks are small enough that dialect, school and style can identify a writer after direct identifiers are removed. Treat any future text collection as identifiable by default.
6. **If this becomes a study in schools:** university ethics approval, the consent arrangements that such research requires, a data protection impact assessment, agreement with the school and its patron body, and a plan to return findings to the school community come before any collection.
7. **Ages and backgrounds of writers are unknown** in every dataset used here. No claim is made about who wrote any text.
