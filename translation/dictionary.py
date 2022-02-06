# much of this is drawn from  https://starwars.fandom.com/wiki/Gungan_Basic
numbers = { # not sure how to handle numbers above 10
    "one": "una",
    "two": "duey",
    "three": "dee",
    "four": "foosa",
    "five": "fife",
    "six": "seeks",
    "seven": "sevin",
    "eight": "ate-a",
    "nine": "ninee",
    "ten": "tenska"
}

common_words = {
    "very": "berry",
    "much": "mui",
    "money": "mula",
    "cash": "mula",
    "capital": "mula",
    "wealth": "mula",
    "salary": "mula",
    "yes": "yesa",
    "no": "nosa",
    "there": "dalee",
    "that": "dat",
    "this": "dis",
    "okay": "okeeday",
    "ok": "okeeday",
    "look": "looky",
    "smiles": "smilin",
    "smile": "smilin",
    "happy": "smilin",
    "speak": "spake",
    "say": "spake",
    "says": "spake",
    "said": "spake",
    "friend": "palo",
    "friends": "palos",
    "pal": "palo",
    "pals": "palos",
    "homie": "palo",
    "homies": "palos",
    "buddy": "palo",
    "buddies": "palos",
    "here": "hair",
    "help": "hep",
    "helps": "heps",
    "human": "hisen",
    "humans": "hisens",
    "story": "tello",
    "stories": "tellos",
    "crazy": "nutsen",
    "nuts": "nutsen",
    "insane": "nutsen",
    "silly": "nutsen",
    "long": "longo",
    "boys": "boyos",
    "mess": "messen",
    "make": "maken",
    "makes": "maken",
    "move": "moven",
    "moves": "moven",
    "machine": "machineek",
    "machines": "machineeks"
}

star_wars_words = {
    "landspeeder": "dowopee",
    "landspeeders": "dowopees",
    "ship": "skeebeetle",
    "ships": "skeebeetles",
    "droid": "machineek",
    "droids": "machineeks",
    "gun": "blaster",
    "guns": "blasters"
}

# there are a lot of words that could translate to bombad
bombad_words = [
    "great", "strong", "awesome", "amazing", "superb", "admirable", "exceptional",
    "remarkable", "excellent", "glorious", "tremendous", "superior", "immense", "heroic",
    "oustanding", "fantastic", "terrific", "marvelous"
]

for word in bombad_words:
    common_words[word] = "bombad"

pronouns = {
    "me": "mesa",
    "my": "mesas",
    "i": "mesa",
    "mine": "mesas",
    "you": "yousa",
    "your": "yous",
    "yours": "yous",
    "he": "hesa",
    "him": "hesa",
    "his": "hes",
    "she": "shesa",
    "her": "shes",
    "hers": "shes",
    "we": "wesa",
    "us": "wesa",
    "our": "wesas",
    "ours": "wesas",
    "they": "daysa",
    "them": "themsa",
    "their": "daysas"
}

gungan_basic = {**numbers, **common_words, **pronouns, **star_wars_words}

# some of the more recognizable words from old gungan, courtesy of: https://starwars.fandom.com/wiki/Old_Gungan
old_gungan = {
    "explosion": "booma",
    "explosions": "boomas",
    "rocket": "bodooka",
    "rockets": "bodookas",
    "floor": "feetwalken",
    "trash": "garbareeno",
    "garbage": "garbareeno",
    "rubbish": "garbareeno",
    "stove": "gasser",
    "drink": "gup",
    "drinks": "gups",
    "wind": "huffmaker",
    "eat": "tongue-grabben",
    "eats": "tongue-grabben",
    "eating": "tongue-grabben",
    "high": "tup",
    "up": "tup",
    "down": "neb"
}

# some of the words we added in, but a lot still taken from gungan basic wookieeepedia. may be updated
our_dict = {
    "are": "isa",
    "is": "isa",
    "hey": "heyo",
    "hi": "hiyo",
    "the": "da",
    "rude": "wude",
    "oh": "oie",
    "boy": "boie",
    "excuse": "ex squeezee",
    "thank": "tank",
    "humble": "humbule",
    "go": "goen",
    "please": "pleasa",
    "food": "foosa",
    "coward": "fraidee frog",
    "cowards": "fraidee frogs",
    "than": "dan",
    "for": "per",
    # "be": "besa",
    "like": "liken",
    "expect": "spect",
    "love": "luv",
    "loves": "luvs",
    "peace": "peles",
    "these": "dese",
    "was": "wasa",
    "were": "wasa",
    "then": "den",
    "with": "wit",
    "without": "witout",
    "something": "sometin",
    "think": "tink",
    "thinking": "tinken",
    "thinkin": "tinken",
    "day": "dayo",
    "cheap": "cheapo",
    "done": "donezo",
    "watch": "watchey",

    # names
    "alex": "alexsa",
    "sydney": "sydsa",
    "kristof": "kristofen",

    # acceptable curse words
    "fuck": "fak",
    "fuckin": "faken",
    "fucking": "faken",
    "shit": "shid",
    "shitted": "shidded",
    "shitten": "shidden",
    "shitting": "shidden",
    "cock": "cawken",
    "dick": "diken",
    "bitch": "bishen",
    "ass": "assa",

    # social media slang
    "twitter": "tweeter",
    "tweet": "tweeten",
    "rt": "retweeten",
    "gg": "good gamen",
    "idk": "mesa no know",
    "idc": "mesa no care",
    "nbd": "no bigen dealo",
    "rn": "right nowsa",
    "kk": "okeeday",
    "u": "yousa",
    "ur": "yous",
    "y": "whysa",
    "r": "isa",
    "pls": "pleasa",
    "plz": "pleasa",
    "yall": "yous",
    "y'all": "yous",
    "imma": "mesa",
    "ion": "mesa no",
    "ain't": "isa not",
    "aint": "isa not",
    "bro": "palo",
    "bros": "palos",

    # contractions
    "he's": "hesa",
    "she's": "shesa",
    "they're": "daysa",
    "we're": "wesa",
    "we'd": "wesa",
    "we've": "wesa",
    "you're": "yousa",
    "you'd": "yousa",
    "you've": "yousa",
    "you'll": "yousa",
    "it's": "isa",
    "he'd": "hesa",
    "he'll": "hesa",
    "she'd": "shesa",
    "she'll": "shesa",
    "that's": "dats",
    "that'd": "dats",
    "there's": "dalees",
    "there're": "dalees",
    "there'd": "daleed",
    "there'll": "dalees",
    "they'd": "daysa",
    "they'll": "daysa",
    "they're": "daysa",
    "they've": "daysa",
    "this's": "dis",
    "who's": "whosa",
    "who're": "whosa",
    "how's": "howsa",
    "how're": "howsa",
    "when's": "whensa",
    "when're": "whensa",
    "what's": "whatsa",
    "what're": "whatsa",
    "where's": "wheresa",
    "why's": "whysa",
    "why're": "whysa",

    # contractions missing apostrophes or without relevant base words
    "im": "mesa",
    "hes": "hesa",
    "shes": "shesa",
    "theyre": "daysa",
    "weve": "wesa",
    "youre": "yousa",
    "youd": "yousa",
    "youve": "yousa",
    "youll": "yousa",
    "don't": "no",
    "dont": "no",
    "didn't": "no",
    "didnt": "no",
    "arent": "isa not",
    "hed": "hesa",
    "thats": "dats",
    "thatd": "dats",
    "theyll": "daysa",
    "theres": "dalees",
    "theyre": "daysa",
    "theyve": "daysa",
    "aren't": "isa not",
    "whos": "whosa",
    "hows": "howsa",
    "howre": "howsa",
    "whens": "whensa",
    "whenre": "whensa",
    "whats": "whatsa",
    "whatre": "whatsa",
    "wheres": "wheresa",
    "whys": "whysa",
    "whyre": "whysa"
}

# our final gungan dictionary
key_words = {**gungan_basic, **old_gungan, **our_dict}

two_phrases = {
    "a lot": "mui",
    "he is ": "hesa ",
    "did he ": "hesa ",
    "did she ": "shesa ",
    "they are ": "daysa ",
    "did they ": "daysa ",
    "you are ": "yousa ",
    "did you ": "yousa ",
    "you guys": "yous",
    "you all": "yous",
    "you lot": "yous",
    "we are ": "wesa ",
    "to be": "besa",
    "it is ": "isa ",
    "who is ": "whosa ",
    "how is ": "howsa ",
    "where is ": "wheresa ",
    "what is ": "whatsa ",
    "when is ": "whensa ",
    "why is ": "whysa ",

    # negations of two phrases
    "he isn't": "hesa not",
    "he isnt": "hesa not",
    "they aren't": "daysa not",
    "they arent": "daysa not",
    "you aren't": "yousa not",
    "you arent": "yousa not",
    "we aren't": "wesa not",
    "we arent": "wesa not",
    "it isn't": "isa not",
    "it isnt": "isa not",

    # our phrases
    "do not": "no",
    "did not": "no",
    " to the": " tada",
    " on the": " onda",
    "see ya": "selongabye",
    "it's a ": "isa ",
    " is a ": " isa "
}

three_phrases = {
    "not doing anything": "doen nutten",
    "see you later": "selongabye",
    "see ya later": "selongabye",
    "all of you": "all-n youse",
    "it is a ": "isa ",
    "into the ": "in tada ", # technically only 2 but needs precedence over "to the"
    "a lot of ": "mui ",
    "i don't know": "my no know",

    # # here because "she is" contains "he is" and so on
    "she is ": "shesa ",
}

four_phrases = {
    "she isn't": "shesa not",
    "she isnt": "shesa not",
    "i do not know": "my now know"
}

i_phrases = {
    "i am": "mesa",
    "i'm": "mesa",
    "i'd": "mesa",
    "i'll": "mesa",
    "i've": "mesa",
}
