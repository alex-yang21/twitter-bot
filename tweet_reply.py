import tweepy
import requests
import json
import logging
import time

import credentials

api_key = credentials.api_key
api_key_secret = credentials.api_key_secret
access_token = credentials.access_token
access_token_secret = credentials.access_token_secret

url = "https://api.funtranslations.com/translate/gungan.json"
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

def get_translation(text):
    """
    Receives the desired text to translate from twitter.
    Returns Gungan translation.
    """
    payload = {"text": text}
    try:
        r = requests.post(url, json=payload)
    except:
        logger.info("Error while translating...")

    json_obj = json.loads(r.text)
    return json_obj["contents"]["translated"]

def get_last_tweet(file):
    f = open(file, 'r')
    line = f.read().strip()
    lastId = 1 # case where not mentioned and restarting code, lastId will stay 1
    if not line: # we have restarted the code, find the most recent mention if any
        logger.info("searching for a previous mention since cold file")
        mentions = api.mentions_timeline()
        for mention in mentions:
            lastId = max(lastId, mention.id)
        lastId += 1 # let's not translate any tweets that are done when down
    else:
        lastId = int(line)
    return lastId

def put_last_tweet(file, Id):
    f = open(file, 'w')
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
    if len(mentions) == 0:
        return

    logger.info("someone mentioned me...")

    for mention in reversed(mentions):
        new_id = mention.id
        if keyword in mention.text.lower(): # chosen keyword above
            logger.info("Responding back to -{}".format(mention.id))
            try:
                logger.info("finding parent tweet")
                replied_tweet = api.get_status(mention.in_reply_to_status_id) # grab the tweet that this mention is replying to
                logger.info("translating tweet")
                translation = get_translation(replied_tweet.text)
                logger.info(f"Tweet: {replied_tweet.text}. Translated tweet: {translation}")
                logger.info("replying to tweet")
                api.update_status(status="@" + mention.user.screen_name + " " + translation, in_reply_to_status_id=mention.id)
            except:
                logger.info("Already replied to {}".format(mention.id))

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
    return res['content']

key_words = {"I", "me", "my", "you", "your", "we", "they", "he", "she", "there", "them", "this", "that", "yes", "no", "one", "two",
              "three", "four", "five", "six", "seven", "eight", "nine", "ten", "very", "great", "superior", "superb", "amazing",
              "okay", "friends", "crazy", "go", "amazing", "happy", "ship", "makes", "rude", "coward", "hello", "machine",
              "here", "help", "floor", "sky", "trash", "God", "god", "wind", "forest", "fire", "love", "rain", "eating", "much",
              "money", "look", "speak", "say", "pals", "human", "story", "long", "make", "boys", "boy"}
key_phrases = ["it is", "a lot", "to be"]

def tweet_quote():
    """
    Tweets the retrieved quote. Attempts to find a quote with at least one of these key words above.
    """
    quote = None
    flag = False
    for i in range(20):
        logger.info("searching for a good quote...")
        quote = get_quote()

        # search quote for key phrases
        for phrase in key_phrases:
            if phrase in quote:
                logger.info("found a quote")
                flag = True
                break

        # search quote for key words
        quote_arr = quote.split()
        for word in quote_arr:
            if word in key_words or "ing" == word[-3:]:
                logger.info("found a quote")
                flag = True
                break

        # wait 3 seconds before calling the API again
        time.sleep(3)

    if not flag:
        logger.info("Didn't find a good quote.")
        return

    logger.info(f"tweeting quote: {quote}")
    translation = get_translation(quote)
    try:
        api.update_status(status='"'+translation'"')
    except:
        logger.info("Failed to tweet quote.")

def main():
    respondToTweet()

if __name__=="__main__":
    main()
