import tweepy
import requests
import json
import logging
import time

import credentials
from translator import get_translation
from dictionary import key_words, two_phrases, three_phrases

api_key = credentials.api_key
api_key_secret = credentials.api_key_secret
access_token = credentials.access_token
access_token_secret = credentials.access_token_secret

url = "https://api.funtranslations.com/translate/gungan.json" # not using anymore
quote_url = "https://api.quotable.io/random"
keyword = "translate"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# For adding logs in application
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
logger.setLevel(logging.INFO)

def get_translation_api(text):
    """
    Receives the desired text to translate from twitter.
    Returns Gungan translation using an online API. No longer used.
    """
    payload = {"text": text}
    try:
        r = requests.post(url, json=payload)
    except:
        logger.info("Error while translating...")

    json_obj = json.loads(r.text)
    return json_obj["contents"]["translated"]

def get_last_tweet(file):
    f = open(file, "r+")
    line = f.read().strip()
    lastId = 0
    if not line: # we have restarted the code, find the most recent mention if any
        logger.info("searching for a previous mention since cold file")
        mentions = api.mentions_timeline()
        for mention in mentions:
            lastId = max(lastId, mention.id)
        lastId += 1 # let's not translate any tweets that are done when down
        f.write(str(lastId))
        logger.info(f"found the last id: {lastId}")
    else:
        logger.info("found most recent reply id, not cold file")
        lastId = int(line)
    f.close()
    return lastId

def put_last_tweet(file, Id):
    f = open(file, "w")
    f.write(str(Id))
    f.close()
    logger.info("Updated the file with the latest tweet Id")

def respondToTweet(file="tweet_id.txt"): # default file
    """
    Checks for mentioned tweets to respond to with translations.
    Stores most recently replied to tweet id in file and writes to with newest one.
    """
    last_id = get_last_tweet(file)
    mentions = api.mentions_timeline(since_id=last_id)

    if len(mentions) == 0: # no new tweets to respond to
        logger.info("no mentions found")
        return

    logger.info("someone mentioned me...")
    new_id = 0
    for mention in reversed(mentions):
        new_id = mention.id
        if keyword in mention.text.lower(): # chosen keyword above
            logger.info("Responding back to {}".format(mention.id))
            replied_tweet = None

            try:
                logger.info("Finding parent tweet")
                replied_tweet = api.get_status(id=mention.in_reply_to_status_id, tweet_mode="extended") # grab the tweet that this mention is replying to
                logger.info(f"Translating tweet: {replied_tweet.full_text}")
                translation = get_translation(replied_tweet.full_text)
                logger.info(f"Translated tweet: {translation}")
                logger.info("Replying to tweet")
                api.update_status(status="@" + mention.user.screen_name + " " + translation, in_reply_to_status_id=mention.id)
            except:
                logger.info("Error in replying or already replied to {}".format(mention.id))

    put_last_tweet(file, new_id)

def get_quote():
    """
    Retrieves quote from quotable.io.
    """
    try:
        response = requests.get(quote_url)
    except:
        logger.info("Error while grabbing the quote.")
    res = json.loads(response.text)
    return res['content'], res['author']

def tweet_quote():
    """
    Tweets the retrieved quote. Attempts to find a quote with at least one of these key words above.
    """
    quote, author = None, None
    flag = False
    for i in range(20):
        logger.info("searching for a good quote...")
        quote, author = get_quote()

        # search quote for key phrases
        for phrase in three_phrases:
            if phrase in quote:
                logger.info(f"found a quote: {quote}")
                flag = True
                break

        for phrase in two_phrases:
            if phrase in quote:
                logger.info(f"found a quote: {quote}")
                flag = True
                break

        # search quote for key words
        quote_arr = quote.split()
        for word in quote_arr:
            if word in key_words or "ing" == word[-3:]:
                logger.info(f"found a quote: {quote}")
                flag = True
                break

        if flag:
            break

        # wait 3 seconds before calling the API again
        time.sleep(3)

    if not flag:
        logger.info("Didn't find a good quote.")
        return

    logger.info(f"tweeting quote: {quote}")
    translation = get_translation(quote)
    try:
        api.update_status(status=f"'{translation}' - {author}")
    except:
        logger.info("Failed to tweet quote.")

def main():
    respondToTweet()

if __name__=="__main__":
    main()
