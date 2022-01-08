from dictionary import key_words, two_phrases, three_phrases

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

    #print(replaced)

    # 2. search the text for any key words and replace
    res = ""
    curr_word = ""
    all_caps = True
    first_cap = True
    for ch in replaced:
        if ch.isalpha() or ch == "'":
            if ch.islower():
                if not curr_word:
                    first_cap = False
                all_caps = False
            curr_word += ch
        else:
            if curr_word.lower() in key_words:
                translated_word = key_words[curr_word.lower()]
                if all_caps:
                    res += translated_word.upper()
                elif first_cap:
                    res += translated_word.capitalize()
                else:
                    res += translated_word
            else:
                 # 3. use randomization rules to spice up the rest
                res += curr_word
            res += ch
            curr_word = ""
            all_caps = True
            first_cap = True

    res += curr_word

    return res
