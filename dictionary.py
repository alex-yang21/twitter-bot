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
    "friend": "pal",
    "friends": "palos",
    "pals": "palos",
    "homies": "palos",
    "buddies": "palos",
    # "go": "gos",
    "here": "hair",
    "help": "hep",
    "helps": "heps",
    "human": "hisen",
    "human": "hisens",
    "story": "tello",
    "stories": "tellos",
    "crazy": "nutsen",
    "nuts": "nutsen",
    "bat-shit": "nutsen",
    "insane": "nutsen",
    "silly": "nutsen",
    "long": "longo",
    "boys": "boyos",
    "hot": "hoten",
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
    "eating": "tongue-grabben"
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

    # contractions
    "i'm": "mesa",
    "he's": "hesa",
    "she's": "shesa",
    "they're": "daysa",
    "we're": "wesa",
    "it's": "isa",
}

# our final gungan dictionary
key_words = {**gungan_basic, **old_gungan, **our_dict}

two_phrases = {
    "a lot": "mui",
    "A LOT": "MUI",
    "i am": "mesa",
    "I am": "mesa",
    "he is": "hesa",
    "He is": "Hesa",
    "HE IS": "HESA",
    "did he": "hesa",
    "Did he": "Hesa",
    "DID HE": "HESA",
    "she is": "shesa",
    "She is": "Shesa",
    "SHE IS": "SHESA",
    "did she": "shesa",
    "Did she": "Shesa",
    "DID SHE": "SHESA",
    "they are": "daysa",
    "They are": "Daysa",
    "THEY ARE": "DAYSA",
    "did they": "daysa",
    "Did they": "Daysa",
    "DID THEY": "DAYSA",
    "you are": "yousa",
    "You are": "Yousa",
    "YOU ARE": "YOUSA",
    "did you": "yousa",
    "Did you": "Yousa",
    "DID YOU": "YOUSA",
    "you guys": "yous",
    "You guys": "Yous",
    "YOU GUYS": "YOUS",
    "you all": "yous",
    "You all": "Yous",
    "YOU ALL": "YOUS",
    "y'all": "yous",
    "Y'all": "Yous",
    "Y'ALL": "YOUS",
    "you lot": "yous",
    "You lot": "Yous",
    "YOU LOT": "YOUS",
    "we are": "wesa",
    "We are": "Wesa",
    "WE ARE": "WESA",
    "to be": "besa",
    "To be": "Besa",
    "TO BE": "BESA",
    "it is": "isa",
    "It is": "Isa",
    "IT IS": "ISA",

    # our phrases
    "do not": "no",
    "Do not": "No",
    "DO NOT": "NO",
    "to the": "tada",
    "To the": "Tada",
    "TO THE": "TADA"
}

three_phrases = {
    "not doing anything": "doen nutten",
    "NOT DOING ANYTHING": "DOEN NUTTEN",
    "see you later": "selongabye",
    "See you later": "Selongabye",
    "SEE YOU LATER": "SELONGABYE",
    "see ya later": "selongabye",
    "See ya later": "Selongabye",
    "SEE YA LATER": "SELONGABYE",
    "all of you": "all-n youse",
    "All of you": "All-n youse",
    "ALL OF YOU": "ALL-N YOUSE"
}
