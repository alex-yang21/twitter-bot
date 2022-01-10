from dictionary import key_words, two_phrases, three_phrases, i_phrases, four_phrases
import spacy

nlp = spacy.load("en_core_web_sm")
good_consonants = {"B", "D", "F", "G", "K", "L", "M", "N", "P", "T", "H", "R", "W", "Z", "X"}

def get_translation(text):
    """
    Takes text of tweet and returns its translation.
    """
    # 1. twitter apostrophes are weird, replace with our apostrophes
    replaced = text.replace("â€™", "'")
    replaced = text.replace("’", "'")

    # 2. Search for noun and verbs that are valid to later modify words
    doc = nlp(replaced)
    valid_nouns = {chunk.root.text for chunk in doc.noun_chunks if chunk.root.tag_ == "NN" and chunk.root.dep_ in ["nsubj", "nsubjpass", "dobj", "pobj"]}
    valid_verbs = {token.text for token in doc if token.tag_ in ["VB", "VBP", "VBZ"]}
    valid_gerunds = {token.text for token in doc if token.tag_ == "VBG"}

    # 3. iterate through key phrases searching for existence and replace
    replaced = replace_phrases(replaced, four_phrases)
    replaced = replace_phrases(replaced, three_phrases)
    replaced = replace_phrases(replaced, two_phrases)
    replaced = replace_phrases(replaced, i_phrases)

    # 4. search the text for any key words and replace
    res = replace_words(replaced, valid_nouns, valid_verbs, valid_gerunds)

    return res

def replace_phrases(replaced, phrases):
    """
    Helper function that takes the given phrases them and replaces them in the text with the relevant translations.
    There are a lot of edge cases with capitalization.
    """
    for phrase in phrases:
        translated_phrase = None

        if phrase in replaced:
            translated_phrase = phrases[phrase]
            replaced = replaced.replace(phrase, translated_phrase)
        elif phrase.upper() in replaced:
            translated_phrase = phrases[phrase]
            replaced = replaced.replace(phrase.upper(), translated_phrase.upper())
        elif phrase.capitalize() in replaced:
            translated_phrase = phrases[phrase]
            replaced = replaced.replace(phrase.capitalize(), translated_phrase.capitalize())

    return replaced

def replace_words(replaced, valid_nouns, valid_verbs, valid_gerunds):
    """
    Helper function that replaces words with their relevant translations.
    """
    res = ""
    curr_word = ""
    replaced += "." # used to make iteration clean
    for i, ch in enumerate(replaced):
        if ch.isalpha() or ch == "'": # can create contractions
            curr_word += ch
        else:
            if curr_word.lower() in key_words:
                translated_word = key_words[curr_word.lower()]
                if curr_word == curr_word.upper() and curr_word.lower() not in {"i", "im"}:
                    res += translated_word.upper()
                elif curr_word == curr_word.capitalize():
                    if curr_word.lower() == "i" and res and res[-1] == " ": # edge case where the word is "I" and in the middle of sentence
                        res += translated_word
                    else:
                        res += translated_word.capitalize()
                else:
                    res += translated_word
            else:
                # use other rules to spice up the non Gungan words
                if curr_word:
                    res += spice_up(curr_word, valid_nouns, valid_verbs, valid_gerunds)
            if i != len(replaced)-1:
                res += ch
            curr_word = ""
    return res

def spice_up(word, valid_nouns, valid_verbs, valid_gerunds):
    """
    Add some gungan type slang to the word.
    """
    all_caps = word == word.upper()

    if word[-3:].lower() == "ing" and word in valid_gerunds: # always change "ing" words to "en"
        if all_caps:
            word = word[:-3] + "EN"
        else:
            word = word[:-3] + "en"
    elif word[-3:].lower() == "ion" and word in valid_nouns: # changes ion to eon
        if all_caps:
            word = word[:-3] + "EON"
        else:
            word = word[:-3] + "eon"
    elif word[-1].lower() == "e" and word in valid_verbs and len(word) > 2 and word[-2].lower() not in "aeiouy":
        if all_caps:
            word += "N"
        else:
            word += "n"
    elif word[-1].upper() in good_consonants and (word in valid_verbs or word in valid_nouns) and len(word) > 2 and word[-2].lower() not in "aeiou":
        if all_caps:
            word += "EN"
        else:
            word += "en"
    return word
