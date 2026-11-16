"""Small hand-built lexicons. All are illustrative and deliberately short.

Sources for the choices are given in docs/overview.md. None of these lists is
a validated instrument.
"""

# The eight English discourse markers and particles that Ó Duibhir and Garland
# (2010) found accounted for most English tokens in immersion pupils' speech.
DISCOURSE_MARKERS = frozenset(
    {"so", "right", "yeah", "no", "just", "like", "then", "okay"}
)

# High-frequency English function words that are not also common Irish word
# forms. Used for a crude lower-bound estimate of English material.
# Deliberately excluded because they are (also) Irish: a, an, is, do, go, as,
# am, sin, he, me, on, at, in, i, be, ar, at, to (tó), had.
ENGLISH_FUNCTION_WORDS = frozenset(
    """the and of that it for with was this but not are from they you have
    what were when your there their which will would about them these
    than been who its our out could should because very really actually
    anyway though also only even still much many some any every where why
    how did does doing done got get gets going want wants need needs know
    think thought said says make made take took see saw look looks good
    great nice bad new old yes maybe never always today tomorrow tonight
    yesterday please thanks thank sorry love hate lol omg btw""".split()
)

# Unaccented spellings of very frequent words whose standard form carries a
# síneadh fada and whose unaccented form is not itself a standard Irish word.
# Ambiguous pairs (ar/ár, ait/áit, fear/féar, leacht/léacht, e/é, me/mé) are
# left out on purpose.
MISSING_FADA = {
    "ta": "tá", "nil": "níl", "bhi": "bhí", "ni": "ní", "tu": "tú",
    "si": "sí", "ca": "cá", "cen": "cén", "la": "lá", "slan": "slán",
    "failte": "fáilte", "feidir": "féidir", "fein": "féin", "mor": "mór",
    "og": "óg", "inne": "inné", "amarach": "amárach", "muinteoir": "múinteoir",
    "leir": "léir", "brea": "breá", "dha": "dhá", "tri": "trí",
    "cuig": "cúig", "eireann": "éireann", "oiche": "oíche", "anios": "aníos",
    "sasta": "sásta", "aris": "arís", "deanamh": "déanamh", "eigin": "éigin",
}

# Text-message initialisms. GRMA is attested in the TwittIrish treebank
# (Cassidy et al. 2022). The others are widely cited informally and are
# included as anecdotal examples only; see docs/overview.md section 5.
ABBREVIATIONS = {
    "grma": "go raibh maith agat",
    "grmma": "go raibh míle maith agat",
    "nasaa": "níl ach saol amháin agat",
}

# A handful of class-membership nouns, for the copula/bí candidate pattern.
CLASS_NOUNS = frozenset(
    """múinteoir dalta buachaill cailín dochtúir feirmeoir duine fear bean
    páiste mac iníon cara scoláire príomhoide altra garda""".split()
)

SUBJECT_PRONOUNS = frozenset(
    {"mé", "tú", "sé", "sí", "muid", "sinn", "sibh", "siad"}
)
BI_FORMS = frozenset({"tá", "níl", "bhí", "beidh", "bhfuil", "raibh"})
