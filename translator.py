from dictionary import key_words, two_phrases, three_phrases
import spacy

nlp = spacy.load("en_core_web_sm")
good_consonants = {"B", "D", "F", "G", "K", "L", "M", "N", "P", "T", "H", "R", "W", "Z", "Y"}

def get_translation(text):
    replaced = text

    # 1. iterate through key phrases searching for existence and replace
    for phrase in three_phrases:
        translated_phrase = None
        if phrase in replaced:
            translated_phrase = three_phrases[phrase]
            replaced = replaced.replace(phrase, translated_phrase)
        elif phrase.upper() in replaced:
            translated_phrase = three_phrases[phrase].upper()
            replaced = replaced.replace(phrase.upper(), translated_phrase)
        elif phrase.capitalize() in replaced:
            translated_phrase = three_phrases[phrase].capitalize()
            replaced = replaced.replace(phrase.capitalize(), translated_phrase)

    for phrase in two_phrases:
        translated_phrase = None
        if phrase in replaced:
            translated_phrase = two_phrases[phrase]
            replaced = replaced.replace(phrase, translated_phrase)
        elif phrase.upper() in replaced:
            translated_phrase = two_phrases[phrase].upper()
            replaced = replaced.replace(phrase.upper(), translated_phrase)
        elif phrase.capitalize() in replaced:
            translated_phrase = two_phrases[phrase].capitalize()
            replaced = replaced.replace(phrase.capitalize(), translated_phrase)

    # 2. Search for noun and verbs that are valid to later modify words
    doc = nlp(replaced)
    valid_nouns = {chunk.root.text for chunk in doc.noun_chunks if chunk.root.tag_ == "NN"}
    valid_verbs = {token.text for token in doc if token.tag_ in {"VB", "VBP", "VBZ"}}

    # 3. if there ever exists 's a ', combine into 'sa '
    replaced = replaced.replace("s a ", "sa ")

    # 4. search the text for any key words and replace
    res = ""
    curr_word = ""
    replaced += "." # used to make iteration clean
    for i, ch in enumerate(replaced):
        if ch.isalpha() or ch == "’":
            curr_word += ch
        else:
            if curr_word.lower() in key_words:
                translated_word = key_words[curr_word.lower()]
                if curr_word == curr_word.upper() and curr_word != "I":
                    res += translated_word.upper()
                elif curr_word == curr_word.capitalize():
                    if curr_word == "I" and res and res[-1] == " ": # edge case where the word is "I" and in the middle of sentence
                        res += translated_word
                    else:
                        res += translated_word.capitalize()
                else:
                    res += translated_word
            else:
                # 4. use othe rules to spice up the rest
                if curr_word:
                    res += spice_up(curr_word, valid_nouns, valid_verbs)
            if i != len(replaced)-1:
                res += ch
            curr_word = ""

    return res

def spice_up(word, valid_nouns, valid_verbs):
    """
    Add some gungan type slang to the word.
    """
    all_caps = word == word.upper()

    if word[-3:].lower() == "ing": # always change "ing" to "en"
        if all_caps:
            word = word[:-3] + "EN"
        else:
            word = word[:-3] + "en"

    elif word[-1].lower() == "e":
        if word in valid_verbs and len(word) > 2 and word[-2].lower() not in "aeiouy" and word[-3].lower() not in "aeiouy":
            if all_caps:
                word += "N"
            else:
                word += "n"
        elif word in valid_nouns and len(word) > 2 and word[-2].lower() not in "scxqzj" and word[-3].lower() not in "scxqzj": # may remove
            if all_caps:
                word += "SA"
            else:
                word += "sa"

    elif word[-1].upper() in good_consonants:
        if len(word) > 2 and word[-2].lower() != "e":
            if word in valid_verbs or word in valid_nouns:
                if all_caps:
                    word += "EN"
                else:
                    word += "en"

    return word
