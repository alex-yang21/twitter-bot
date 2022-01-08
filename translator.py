from dictionary import key_words, two_phrases, three_phrases
import random
from itertools import accumulate
from operator import add
import spacy

nlp = spacy.load("en_core_web_sm")
good_consonants = {"B", "D", "F", "G", "K", "L", "M", "N", "P", "S", "T", "H", "R", "W", "Z", "Y"}

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

    # 2. Search for noun chunks and for later to modify words that are root nouns
    doc = nlp(replaced)
    valid_nouns = set()
    for chunk in doc.noun_chunks:
        valid_nouns.add(chunk.root.text)

    # 3. if there ever exists 's a ', combine into 'sa '
    replaced = replaced.replace("s a ", "sa ")

    # 4. search the text for any key words and replace
    res = ""
    curr_word = ""
    replaced += "." # used to make iteration clean
    for i, ch in enumerate(replaced):
        if ch.isalpha() or ch == "'":
            curr_word += ch
        else:
            if curr_word.lower() in key_words:
                translated_word = key_words[curr_word.lower()]
                # we keep note of what capitalization the user may have had
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
                    res += spice_up(curr_word, valid_nouns)
            if i != len(replaced)-1:
                res += ch
            curr_word = ""

    return res

def spice_up(word, valid_nouns):
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
        doc = nlp(word)
        word_type = doc[0].tag_
        if word_type in {"VB", "VBP", "VBZ"}:
            if all_caps:
                word += "N"
            else:
                word += "n"
        elif word_type == "NN" and len(word) > 1 and word[-2].lower() != "s" and word in valid_nouns: # may remove
            if all_caps:
                word += "SA"
            else:
                word += "sa"

    elif word[-1].upper() in good_consonants:
        if len(word) > 1 and word[-2].lower() not in {"a", "e", "i", "o", "u", "y"}:
            doc = nlp(word)
            word_type = doc[0].tag_
            if word_type in {"VB", "VBP", "VBZ"} or (word_type == "NN" and word in valid_nouns):
                if all_caps:
                    word += "EN"
                else:
                    word += "en"

    return word
