from dictionary import key_words, two_phrases, three_phrases, i_phrases, four_phrases
import spacy
from spacy_syllables import SpacySyllables
import re

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("syllables", after="tagger")
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
    two_or_less_syllables = {token.text for token in doc if token._.syllables_count and token._.syllables_count <= 2}

    # 3. Use the 'I am going' -> 'My going' rule, the 'going' will change to 'goen' later. We change to 'myalex' to avoid double translation.
    replaced = grammar_rule(replaced)

    # 4. iterate through key phrases searching for existence and replace
    replaced = replace_phrases(replaced, four_phrases)
    replaced = replace_phrases(replaced, three_phrases)
    replaced = replace_phrases(replaced, two_phrases)
    replaced = replace_phrases(replaced, i_phrases)

    # 5. search the text for any key words and replace
    replaced = replace_words(replaced, valid_nouns, valid_verbs, valid_gerunds, two_or_less_syllables)

    # 6. Replace the 'myalex' with 'my'
    replaced = replaced.replace("myalex", "my")
    replaced = replaced.replace("Myalex", "My")
    replaced = replaced.replace("MYalex", "MY")

    return replaced

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
            if phrases == i_phrases:
                replaced = replaced.replace(phrase.upper(), translated_phrase)
            else:
                replaced = replaced.replace(phrase.upper(), translated_phrase.upper())
        elif phrase.capitalize() in replaced:
            translated_phrase = phrases[phrase]
            if phrases == i_phrases:
                replaced = replaced.replace(phrase.capitalize(), translated_phrase)
            else:
                replaced = replaced.replace(phrase.capitalize(), translated_phrase.capitalize())

    return replaced

def replace_words(replaced, valid_nouns, valid_verbs, valid_gerunds, two_or_less_syllables):
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
                    res += spice_up(curr_word, valid_nouns, valid_verbs, valid_gerunds, two_or_less_syllables)
            if i != len(replaced)-1:
                res += ch
            curr_word = ""
    return res

def spice_up(word, valid_nouns, valid_verbs, valid_gerunds, two_or_less_syllables):
    """
    Add some gungan type slang to the word.
    """
    all_caps = word == word.upper()

    if word[-3:].lower() == "ing" and word in valid_gerunds and len(word) > 5 and word[-4] != "e": # change "ing" words to "en"
        if all_caps:
            word = word[:-3] + "EN"
        else:
            word = word[:-3] + "en"
    elif word[-3:].lower() == "ion" and word in valid_nouns: # changes ion to eon
        if all_caps:
            word = word[:-3] + "EON"
        else:
            word = word[:-3] + "eon"
    elif word[-1].lower() == "e" and word in valid_verbs and len(word) > 2 and word[-2].lower() not in "aeiouy" and word in two_or_less_syllables:
        if all_caps:
            word += "N"
        else:
            word += "n"
    elif word[-1].upper() in good_consonants and (word in valid_verbs or word in valid_nouns) and len(word) > 2 and word[-2].lower() not in "aeiou" and word in two_or_less_syllables:
        if all_caps:
            word += "EN"
        else:
            word += "en"
    return word

def grammar_rule(replaced):
    """
    Change instances of 'my going' -> 'my goen' per https://starwars.fandom.com/wiki/Gungan_Basic.
    We want to maintain capitalization so we do a few different regex substitutions.
    """
    # all uppercase MY
    exp1 = r"\bI AM (\b[a-zA-Z]+(ing|ING)\b)"
    exp2 = r"MYalex \1"
    replaced = re.sub(exp1, exp2, replaced)

    # capitalized 'My; for beginning of sentences
    exp3 = r"(\. |\. )I am (\b[a-zA-Z]+(ing|ING)\b)"
    exp4 = r"\1Myalex \2"
    replaced = re.sub(exp3, exp4, replaced)

    # lowercase 'my' with a space
    exp5 = r"( |\.|\. )[Ii] am (\b[a-zA-Z]+(ing|ING)\b)" # we do it in the order given, that way we keep a ? for the white space
    exp6 = r"\1myalex \2"
    replaced = re.sub(exp5, exp6, replaced)

    # capitalized 'My' for beginning of entire text
    exp7 = r"\bI am (\b[a-zA-Z]+(ing|ING)\b)"
    exp8 = r"Myalex \1"
    replaced = re.sub(exp7, exp8, replaced)

    # lowercase 'my' for beginning of entire text
    exp9 = r"\bi am (\b[a-zA-Z]+(ing|ING)\b)"
    exp10 = r"myalex \1"
    replaced = re.sub(exp9, exp10, replaced)

    return replaced
