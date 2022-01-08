from dictionary import key_words, two_phrases, three_phrases
import random
from itertools import accumulate
from operator import add

def get_translation(text):
    # need to figure out a way to maintain capitilizations
    replaced = text
    # 1. iterate through key phrases searching for existence and replace
    for phrase in three_phrases:
        translated_phrase = three_phrases[phrase]
        replaced = replaced.replace(phrase, translated_phrase)

    for phrase in two_phrases:
        translated_phrase = two_phrases[phrase]
        replaced = replaced.replace(phrase, translated_phrase)

    # 2. if there are ever exists 's a ', combine into 'sa '
    replaced = replaced.replace("s a ", "sa ")

    # 3. search the text for any key words and replace
    res = ""
    curr_word = ""
    all_caps = True
    first_cap = True
    replaced += "." # used to make iteration clean
    for i, ch in enumerate(replaced):
        if ch.isalpha() or ch == "'":
            if ch.islower():
                if not curr_word:
                    first_cap = False
                all_caps = False
            curr_word += ch
        else:
            if curr_word.lower() in key_words:
                translated_word = key_words[curr_word.lower()]
                # we keep note of what capitalization the user may have had
                if all_caps:
                    res += translated_word.upper()
                elif first_cap:
                    res += translated_word.capitalize()
                else:
                    res += translated_word
            else:
                # 4. use randomization rules to spice up the rest
                if curr_word:
                    res += spice_up(curr_word)
            if i != len(replaced)-1:
                res += ch
            curr_word = ""
            all_caps = True
            first_cap = True

    return res

def random_choice(probs):
    """
    probs is an array of that maps percentages to indices for our choices.
    Return an indice that is the choice we go with.
    """
    cum_sum = accumulate(probs, add)
    cum_sum = list(cum_sum)
    cum_sum.append(1.0)
    val = random.random()
    for index, lvl in enumerate(cum_sum):
        if val < lvl:
            return index
    return -1 # should never be returned

good_consonants = {"B", "D", "F", "G", "K", "L", "M", "N", "P", "S", "T", "H", "R", "W", "Z", "Y"}

def spice_up(word):
    """
    Add some gungan type slang to the word.
    """
    ing_probs = [.5, .5] # index 0 represents replace "ing" with "en", index 1 represents remove "ing" altogether
    s_probs = [.2] # index 0 represents add "a" after a word that ends in "s"
    e_probs = [.25, .1] # index 0 represents add "n" to a word that ends in "e", index 1 represents add "sa"
    cons_probs = [.15] # index 0 represents adding "en" to a word that ends in a "good consonant"

    all_caps = word == word.upper()

    if word[-3:].lower() == "ing":
        choice = random_choice(ing_probs)
        if choice == 0:
            if all_caps:
                word = word[:-3] + "EN"
            else:
                word = word[:-3] + "en"
        elif choice == 1:
            word = word[:-3]
    elif word[-1].lower() == "s":
        choice = random_choice(s_probs)
        if choice == 0:
            if all_caps:
                word += "A"
            else:
                word += "a"
    elif word[-1].lower() == "e":
        choice = random_choice(e_probs)
        if choice == 0:
            if all_caps:
                word += "N"
            else:
                word += "n"
        elif choice == 1:
            if all_caps:
                word += "SA"
            else:
                word += "sa"
    elif word[-1].upper() in good_consonants:
        choice = random_choice(cons_probs)
        if choice == 0:
            if all_caps:
                word += "EN"
            else:
                word += "en"
    return word
