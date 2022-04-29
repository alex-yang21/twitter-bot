from app import logger

off_limits = {
    # off limit words
    "nigger",
    "nigga",
    "niglet",
    "midget",
    "fag",
    "kms",
    "kill myself",
    "chink",
    "chinaman",
    "ching chong",
    "coon",
    "cunt",
    "dyke",
    "gook",
    "heeb",
    "kike",
    "dago",
    "beaner",
    "retard",
    "autist",
    "nazi",
    "hitler",
    "slut",
    "whore",
    "homo ",
    "gay ",
    "queer",
    "inbred",
    "camel jockey",
    "darky",
    "darkie",
    "darkey",
    " jap ",
    "twink",
    "cripple",
    "transgender",
    "prostitute",
    "hooker",
    "ghetto",

    # off limit events
    "holocaust",
    "genocide",
    "9/11",
    "ethnic cleansing",
    "apartheid",
    "casualty",
    "casualties",
    "terrorist",
    "murder",

    # sexual
    " anal ",
    "anus",
    "blowjob",
    "blow job",
    " bj ",
    "buttplug",
    "clitoris",
    "dildo",
    "fellate",
    "fellatio",
    "labia",
    "scrotum",
    "porn",
    "penis",
    "pussy",
    "vagina",
    " cum ",

    " rape ",
    " rapist ",
    "molest",
    "incest",
    "beastiality",
    "necrophil",
    "pedophile",
    "abortion",

    # religions
    "christians",
    "christianity",
    "islam",
    "muslim",
    "hindu",
    " jew ",
    "jewish",
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
    "putin",
}

def is_profane(text):
    """
    Helper function that checks if a text contains profanity.
    """
    lower_case = text.lower()
    for word in off_limits:
        if word in lower_case:
            logger.info(f"Found banned word: {word}")
            return True
    return False
