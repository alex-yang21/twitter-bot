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
    "friends": "palos",
    "pals": "palos",
    "homies": "palos",
    "buddies": "palos",
    # "go": "gos",
    "here": "hair",
    "help": "hep",
    "human": "hisen",
    "story": "tello",
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
    "plane": "dowopee",
    "car": "dowopee",
    "train": "dowopee",
    "helicopter": "dowopee"
    "ship": "skeebeetle",
    "droid": "machineek",
    "droids": "machineeks"
}

# there are a lot of words that could translate to bombad
bombad_words = [
    "great", "strong", "awesome", "amazing", "superb", "admirable", "exceptional",
    "remarkable", "excellent", "glorious", "tremendous", "superior",
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
    "them": "themsa"
}

gungan_basic = numbers | common_words | pronouns | star_wars_words

# some of the more recognizable words from old gungan, courtesy of: https://starwars.fandom.com/wiki/Old_Gungan
old_gungan = {
    "gun": "booma",
    "explosion": "booma",
    "rocket": "bodooka",
    "floor": "feetwalken",
    "trash": "garbareeno",
    "garbage": "garbareeno",
    "stove": "gasser",
    "drink": "gup",
    "wind": "huffmaker",
    "eat": "tongue-grab",
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
    "than": "dan",
    "for": "per",
    "be": "besa"
}

# our final gungan dictionary
gungan = gungan_basic | old_gungan | our_dict

short_phrases = {
    "a lot": "mui",
    "i am": "mesa",
    "i'm": "mesa", # can't forget contractions
    "he is": "hesa",
    "he's": "hesa",
    "did he": "hesa",
    "she is": "shesa",
    "she's": "shesa",
    "did she": "shesa",
    "they are": "daysa",
    "they're": "daysa",
    "did they": "daysa"
    "you are": "yousas",
    "did you": "yousas",
    "you guys": "yous",
    "you all": "yous",
    "you lot": "yous",
    "all of you":" all-n youse",
    "we are": "wesa",
    "we're": "wesa",
    "to be": "besa",
    "it is": "isa"
}

long_phrases = {
    "not doing anything": "doen nutten",
    "see you later": "selongabye"
}

# we may add to this
our_phrases = {
    "do not": "no",
}

# our final group of phrases
phrases = short_phrases | long_phrases | our_phrases
