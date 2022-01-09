# much of this is drawn from  https://starwars.fandom.com/wiki/Gungan_Basic
numbers = { # not sure how to handle numbers above 10
    "one": "una",
    "1": "una",
    "two": "duey",
    "2": "duey",
    "three": "dee",
    "3": "dee",
    "four": "foosa",
    "4": "foosa",
    "five": "fife",
    "5": "fife",
    "six": "seeks",
    "6": "seeks",
    "seven": "sevin",
    "7": "sevin",
    "eight": "ate-a",
    "8": "ate-a",
    "nine": "ninee",
    "9": "ninee",
    "ten": "tenska",
    "10": "tenska"
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
    "happy": "smilin",
    "speak": "spake",
    "say": "spake",
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
    "plane": "dowopee",
    "planes": "dowopees",
    "car": "dowopee",
    "cars": "dowopees",
    "train": "dowopee",
    "trains": "dowopees",
    "helicopter": "dowopee",
    "helicopters": "dowopees",
    "ship": "skeebeetle",
    "ships": "skeebeetles",
    "droid": "machineek",
    "droids": "machineeks"
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
    "my": "mesa",
    "i": "mesa",
    "mine": "mesas",
    "you": "yousa",
    "your": "yous",
    "yours": "yous",
    "he": "hesa",
    "him": "hesa",
    "his": "hesas",
    "she": "shesa",
    "her": "shesa",
    "hers": "shesas",
    "we": "wesa",
    "us": "wesa",
    "our": "wesa",
    "ours": "wesa",
    "they": "daysa",
    "them": "themsa",
    "their": "daysa"
}

gungan_basic = {**numbers, **common_words, **pronouns, **star_wars_words}

# some of the more recognizable words from old gungan, courtesy of: https://starwars.fandom.com/wiki/Old_Gungan
old_gungan = {
    "gun": "booma",
    "guns": "boomas",
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
    #"be": "besa",
    "like": "liken",
    "expect": "spect",
    "love": "luv",
    "loves": "luvs",
    "peace": "peles",
    "invitation": "invitateon",
    "invitations": "invitateons",
    "these": "dese",
    "was": "wasa",
    "were" : "wasa",
    "then": "den",

    # names
    "alex": "alexsa",
    "sydney": "sydsa",
    "kristof": "kristofen",
    "cock": "cawk",

    # contractions and slang
    "i'm": "mesa",
    "im": "mesa",
    "i'd": "mesa",
    "i'll": "mesa",
    "i've": "mesa",
    "he's": "hesa",
    "hes": "hesa",
    "she's": "shesa",
    "shes": "shesa",
    "they're": "daysa",
    "theyre": "daysa",
    "their": "daysas",
    "we're": "wesa",
    "we'd": "wesa",
    "we've": "wesa",
    "weve": "wesa",
    "you're": "yousa",
    "youre": "yousa",
    "ur": "yousa",
    "you'd": "yousa",
    "youd": "yousa",
    "you've": "yousa",
    "youve": "yousa",
    "you'll": "yousa",
    "youll": "yousa",
    "it's": "isa",
    "don't" : "no",
    "dont": "no",
    "didn't": "no",
    "didnt": "no",
    "ain't": "isa not",
    "aint": "isa not",
    "aren't": "isa not",
    "arent": "isa not",
    "he'd": "hesa",
    "hed": "hesa",
    "he'll": "hesa",
    "she'd": "shesa",
    "she'll": "shesa",
    "imma": "mesa",
    "ion": "mesa no",
    "that's": "dats",
    "thats": "dats",
    "that'd": "dats",
    "thatd": "dats",
    "there's": "dalees",
    "theres": "dalees",
    "there're": "dalees",
    "there'd": "daleed",
    "there'll": "dalees",
    "they'd": "daysa",
    "they'll": "daysa",
    "theyll": "daysa",
    "they're": "daysa",
    "theyre": "daysa",
    "they've": "daysa",
    "theyve": "daysa",
    "this's": "dis",
    "who's": "whosa",
    "whos": "whosa",
    "who're": "whosa",
    "how's": "howsa",
    "hows": "howsa",
    "how're": "howsa",
    "howre": "howsa",
    "when's": "whensa",
    "whens": "whensa",
    "when're": "whensa",
    "whenre": "whensa",
    "what's": "whatsa",
    "whats": "whatsa",
    "what're": "whatsa",
    "whatre": "whatsa",
    "where's": "wheresa",
    "wheres": "wheresa",
    "why's": "whysa",
    "whys": "whysa",
    "why're": "whysa",
    "whyre": "whysa",
    "y'all": "yous",
    "yall": "yous",

    # social media slang
    "rt": "retweeten",
    "gg": "good gamen",
    "idk": "mesa no know",
    "idc": "mesa no care",
    "nbd": "no bigen dealo",
    "rn": "right nowsa",
    "kk": "okeeday",
}

# our final gungan dictionary
key_words = {**gungan_basic, **old_gungan, **our_dict}

two_phrases = {
    "a lot": "mui",
    "i am": "mesa",
    "i was": "mesa",
    "he is": "hesa",
    "he was": "hesa",
    "did he": "hesa",
    "she is": "shesa",
    "she was": "shesa",
    "did she": "shesa",
    "they are": "daysa",
    "they were": "daysa",
    "did they": "daysa",
    "you are": "yousa",
    "you were": "yousa",
    "did you": "yousa",
    "you guys": "yous",
    "you all": "yous",
    "you lot": "yous",
    "we are": "wesa",
    "we were": "wesa",
    "to be": "besa",
    "it is": "isa",
    "it was": "isa",
    "who is": "whosa",
    "who was": "whosa",
    "who were": "whosa",
    "how is": "howsa",
    "how was": "howsa",
    "how were": "howsa",
    "where is": "wheresa",
    "where was": "wheresa",
    "where were": "wheresa",
    "what is": "whatsa",
    "what was":" whatsa",
    "what were": "whatsa",
    "when is": "whensa",
    "when was": "whensa",
    "when were": "whensa",
    "why is": "whysa",
    "why was": "whysa",
    "why were": "whysa",

    # our phrases
    "do not": "no",
    "did not": "no",
    "to the": "tada",
    "see ya": "selongabye",
    "it's a": "isa"
}

three_phrases = {
    "not doing anything": "doen nutten",
    "see you later": "selongabye",
    "see ya later": "selongabye",
    "all of you": "all-n youse",
    "it is a": "isa"
}
