import tweepy
import requests
import json
import logging
import time

import credentials
from translator import get_translation
from dictionary import key_words, two_phrases, three_phrases, i_phrases

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
    """
    Reads from file the tweet id that we last replied to.
    """
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
    """
    Writes to file the tweet id that we just replied to.
    """
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
    return res["content"], res["author"]

def tweet_quote():
    """
    Tweets the retrieved quote. Attempts to find a quote with at least one key word or phrase.
    """
    quote, author = None, None
    flag = False
    for i in range(20):
        logger.info("searching for a good quote...")
        quote, author = get_quote()

        # search quote for key phrases
        flag = find_phrases(quote, three_phrases) or find_phrases(quote, two_phrases) or find_phrases(quote, i_phrases)

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
        logger.info("Didn't find a good quote. Try again tomorrow.")
        return

    logger.info(f"tweeting quote: {quote}")
    translation = get_translation(quote)
    try:
        api.update_status(status=f"'{translation}' - {author}")
    except:
        logger.info("Failed to tweet quote.")

def find_phrases(quote, phrases):
    """
    Helper function to find phrases.
    """
    for phrase in phrases:
        if phrase in quote:
            logger.info(f"found a quote: {quote}")
            return True
    return False

def get_tweet_text(dm):
    """
    Gets tweet text from a direct message.
    """
    return dm._json["message_create"]["message_data"]["text"]

def get_tweet_url(dm):
    """
    Gets tweet id from a direct message if a tweet is sent. Else return -1
    """
    dm_data = dm._json["message_create"]["message_data"]
    urls = dm_data["entities"]["urls"]
    url = None
    if urls:
        url = urls[0]["expanded_url"]
        logger.info(f"found url: {url}")
        url_arr = url.split("/")
        return url

def get_last_dm(file="dm_id.txt"):
    """
    Reads from file the dm id that we last fulfilled. Or finds the most recent dm id.
    """
    f = open(file, "r+")
    line = f.read().strip()
    lastId = 1
    if not line: # we have restarted the code, find the most recent mention if any
        logger.info("searching for a previous dm since cold file")
        dms = api.get_direct_messages(count=5)
        if dms:
            lastId = int(dms[0]._json["id"]) # sorted in reverse chronological order
            f.write(str(lastId))
            text = get_tweet_text(dms[0])
            logger.info(f"found the last dm. id: {lastId}, text: {text}")
    else:
        lastId = int(line)
        logger.info(f"found most recent dm id on file: {lastId}")

    f.close()
    return lastId


def reply_dms(file="dm_id.txt"):
    """
    Checks for direct messages of tweets to respond to with translations.
    Stores most recently fulfilled dm id in file and writes to with newest one.
    """
    last_id = get_last_dm(file)
    if last_id == 1:
        logger.info("No dms yet")
        return

    dms = api.get_direct_messages(count=20) # don't anticipate doing more than 20 dms per day

    dm_id, url = 0, None
    flag = False
    for dm in reversed(dms): # start with oldest dm first
        text = get_tweet_text(dm)
        dm_id = dm._json["id"]
        url = get_tweet_url(dm)
        logger.info(f"Getting dm. ID: {dm_id}, tweet text: {text}")
        if not url:
            logger.info("DM had no associated tweet")
            continue
        if dm_id > last_id: # checks if any new DMs
            flag = True
            logger.info("someone dmed me...")
            logger.info("Replying back to {}".format(dm_id))
            tweet = None
            try:
                logger.info("Finding tweet")
                tweet = api.get_status(id=dm_id, tweet_mode="extended")
                logger.info(f"Translating tweet: {tweet.full_text}")
                translation = get_translation(tweet.full_text)
                logger.info(f"Translated tweet: {translation}")
                logger.info("Replying to tweet")
                api.update_status(status=translation, attachment_url=url)
            except:
                logger.info("Error in replying or already replied to {}".format(dm_id))

    if flag:
        put_last_tweet(file, dm_id)
    else:
        logger.info("No new dms found")

def main():
    respondToTweet()

if __name__=="__main__":
    main()
