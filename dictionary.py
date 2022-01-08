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
    "human": "hisens",
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
    "stove": "gasser",
    "drink": "gup",
    "drinks": "gups",
    "wind": "huffmaker",
    "eat": "tongue-grab",
    "eats": "tongue-grabs",
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
    "be": "besa",
    "like": "liken",
    "expect": "spect",
    "love": "luv",
    "loves": "luvs",
    "peace": "peles",
    "invitation": "invitateon",
    "invitations": "invitateons",
    "these": "dese",

    # names
    "alex": "alexsa",
    "sydney": "sydsa",
    "kristof": "kristofen",

    # contractions
    "i'm": "mesa",
    "i'd": "mesa",
    "i'll": "mesa",
    "i've": "mesa",
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
    "don't" : "no",
    "didn't": "no",
    "ain't": "isa not",
    "aren't": "isa not",
    "he'd": "hesa",
    "he'll": "hesa",
    "she'd": "shesa",
    "she'll": "shesa",
    "imma": "mesa",
    "ion": "mesa no",
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
    "this's": "dis"
}

# our final gungan dictionary
key_words = {**gungan_basic, **old_gungan, **our_dict}

two_phrases = {
    "a lot": "mui",
    "i am": "mesa",
    "he is": "hesa",
    "did he": "hesa",
    "she is": "shesa",
    "did she": "shesa",
    "they are": "daysa",
    "did they": "daysa",
    "you are": "yousa",
    "did you": "yousa",
    "you guys": "yous",
    "you all": "yous",
    "y'all": "yous",
    "you lot": "yous",
    "we are": "wesa",
    "to be": "besa",
    "it is": "isa",

    # our phrases
    "do not": "no",
    "did not": "no",
    "to the": "tada",
    "see ya": "selongabye",
}

three_phrases = {
    "not doing anything": "doen nutten",
    "see you later": "selongabye",
    "see ya later": "selongabye",
    "all of you": "all-n youse"
}
