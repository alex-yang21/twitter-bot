import tweepy
import requests
import json
import logging

import credentials

api_key = credentials.api_key
api_key_secret = credentials.api_key_secret
access_token = credentials.access_token
access_token_secret = credentials.access_token_secret

url = "https://api.funtranslations.com/translate/gungan.json"
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
        print("Error while translating...")

    json_obj = json.loads(r.text)
    return json_obj["contents"]["translated"]

def get_last_tweet(file):
    f = open(file, 'r')
    lastId = int(f.read().strip())
    f.close()
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
    mentions = api.mentions_timeline(last_id, tweet_mode='extended')
    if len(mentions) == 0:
        return

    logger.info("someone mentioned me...")

    for mention in reversed(mentions):
        new_id = mention.id
        if keyword in mention.full_text.lower(): # chosen keyword above
            logger.info("Responding back to -{}".format(mention.id))
            try:
                replied_tweet = api.get_status(mention.in_reply_to_status_id) # grab the tweet that this mention is replying to
                translation = get_translation(replied_tweet.text)
                logger.info("liking and replying to tweet")
                api.create_favorite(mention.id)
                api.update_status('@' + mention.user.screen_name + " " + translation, mention.id)
            except:
                logger.info("Already replied to {}".format(mention.id))

    put_last_tweet(file, new_id)

if __name__=="__main__":
    respondToTweet()
