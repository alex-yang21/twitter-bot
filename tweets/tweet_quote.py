import requests
import json
import time

from application import api
from application import logger

from translator import get_translation
from dictionary import key_words, two_phrases, three_phrases, i_phrases

quote_url = "https://api.quotable.io/random"

def get_quote():
    """
    Retrieves quote from quotable.io.
    """
    try:
        response = requests.get(quote_url)
    except:
        logger.info("Error while grabbing the quote.")
    res = json.loads(response.text)
    return res["content"], res["author"]

def tweet_daily_quote():
    """
    Tweets the retrieved quote. Attempts to find a quote with at least one key word or phrase.
    """
    quote, author = None, None
    flag = False
    for i in range(20):
        logger.info("searching for a good quote...")
        quote, author = get_quote()
        if is_good_text(quote):
            break

        # wait 3 seconds before calling the API again
        time.sleep(3)

    if not flag:
        logger.info("Didn't find a good quote. Try again tomorrow.")
        return

    logger.info(f"tweeting quote: {quote}")
    translation = get_translation(quote)
    try:
        api.update_status(status=f"'{translation}' - {author}")
    except:
        logger.info("Failed to tweet quote.")

def is_good_text(text):
    """
    Helper function that returns True if the text contains a word we can translate.
    """
    # search text for phrases
    if find_phrases(text, three_phrases) or find_phrases(text, two_phrases) or find_phrases(text, i_phrases):
        return True

    # search text for key words
    text_arr = text.split()
    for word in text_arr:
        if word in key_words:
            logger.info(f"text contains a keyword: {text}")
            return True

    return False

def find_phrases(text, phrases):
    """
    Helper function to find "good" phrases.
    """
    for phrase in phrases:
        if phrase in text:
            logger.info(f"text contains a phrase: {text}")
            return True
    return False
