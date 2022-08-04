from app import logger

off_limit_words = {
    "nigger",
    "niggers",
    "niggerz",
    "nigga",
    "niggas",
    "niggaz",
    "niglet",
    "niglets",
    "midget",
    "midgets",
    "fag",
    "fags",
    "fagz",
    "faggot",
    "faggots",
    "faggotz",
    "fag1t",
    "faget",
    "fagg1t",
    "faggit",
    "fagg0t",
    "fagit",
    "faig",
    "faigs",
    "kms",
    "chink",
    "chinks",
    "chinaman",
    "coon",
    "coons",
    "cunt",
    "cunts",
    "dyke",
    "dykes",
    "gook",
    "gooks",
    "heeb",
    "kike",
    "kikes",
    "dago",
    "beaner",
    "retard",
    "retards",
    "retarded",
    "autist",
    "autists",
    "autistic",
    "nazi",
    "nazis",
    "hitler",
    "slut",
    "sluts",
    "whore",
    "whores",
    "hoe",
    "homo",
    "gay",
    "gays",
    "queer",
    "queers",
    "inbred",
    "darky",
    "darkie",
    "darkies",
    "darkey",
    "jap",
    "twink",
    "twinks",
    "cripple",
    "cripples",
    "transgender",
    "tranny",
    "trannies",
    "shemale",
    "prostitute",
    "prostitutes",
    "hooker",
    "hookers",
    "ghetto",

    # off limit events
    "holocaust",
    "genocide",
    "nine-eleven",
    "apartheid",
    "casualty",
    "casualties",
    "terrorist",
    "murder",
    "murders",
    "shooting",
    "shootings",

    # sexual
    "anal",
    "anus",
    "blowjob",
    "buttplug",
    "buttplugs",
    "clit",
    "clitoris",
    "dildo",
    "dildos",
    "fellate",
    "fellatio",
    "labia",
    "masturbate",
    "masturbates",
    "masturbator",
    "masturbators",
    "masturbating",
    "orgasm",
    "scrotum",
    "porn",
    "pornography",
    "penis",
    "penises",
    "pussy",
    "pussies",
    "vagina",
    "vaginas",
    "cum",
    "cums",

    "rape",
    "rapes",
    "rapist",
    "rapists",
    "molest",
    "molests",
    "molestor",
    "incest",
    "beastiality",
    "necrophil",
    "pedophile",
    "pedophiles",
    "pedophilia",
    "abortion",
    "abortions",

    # religions
    "christian",
    "christians",
    "christianity",
    "islam",
    "muslim",
    "muslims",
    "hijab",
    "hinduism",
    "hindu",
    "hindus",
    "judaism",
    "jew",
    "jewish",
    "buddha",
    "buddhism",
    "buddhist",

    # health related
    "hiv",
    "aids",
    "herpes",
    "dementia",
    "alzheimers",
    "alzheimer's",
    "cancer",

    # Russia Ukraine conflict related
    "russia",
    "ukraine",
}

off_limit_phrases = {
    "kill myself",
    "ching chong",
    "camel jockey",
    "blow job",
    "butt plug",
    "nine eleven",
    "ethnic cleansing",
    "9/11"
}

def is_profane(text):
    """
    Helper function that checks if a text contains profanity.
    """
    logger.info("Checking for profanity")
    lower_case = text.lower()
    curr_word = ""
    for ch in lower_case:
        if ch.isalpha():
            curr_word += ch
        else:
            if curr_word in off_limit_words:
                logger.info(f"Found banned word: {curr_word}")
                return True
            curr_word = ""

    if curr_word in off_limit_words:
        logger.info(f"Found banned word: {curr_word}")
        return True

    for phrase in off_limit_phrases:
        if phrase in lower_case:
            logger.info(f"Found banned phrase: {phrase}")
            return True

    return False
