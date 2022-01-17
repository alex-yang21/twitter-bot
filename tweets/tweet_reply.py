import re

from app import api
from app import logger

from translation.translator import get_translation
from translation.banned_words import is_profane

keyword = "translate"

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

def respond_to_tweet(file):
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
            logger.info(f"Responding back to {mention.id}")
            replied_tweet = None

            try:
                logger.info("Finding parent tweet")
                replied_tweet = api.get_status(id=mention.in_reply_to_status_id, tweet_mode="extended") # grab the tweet that this mention is replying to
                logger.info(f"Translating tweet: {replied_tweet.full_text}")
                logger.info("Checking for profanity")

                if is_profane(replied_tweet.full_text):
                    assert 1 == 2 # fail the try block

                # truncate the tweet text to be below 280 character limit if possible
                truncated = re.sub(r' https://t.co/\w{10}', '', replied_tweet.full_text) # replace annoying url at end
                truncated = re.sub(' +', ' ', truncated) # replace all unnecessary white space
                translation = get_translation(truncated)
                logger.info(f"Translated tweet: {translation}")

                translated_tweet = None
                if len(translation) > 280:
                    logger.info("Translation longer than 280 characters")
                    first, second = translation[:280], translation[280:]
                    logger.info(f"Replying with first part: {first}")
                    translated_tweet = api.update_status(status="@" + mention.user.screen_name + " " + first, in_reply_to_status_id=mention.id)
                    logger.info(f"Replying with second part: {second}")
                    api.update_status(status=second, in_reply_to_status_id=translated_tweet.id)
                else:
                    logger.info("Replying to tweet")
                    api.update_status(status="@" + mention.user.screen_name + " " + translation, in_reply_to_status_id=mention.id)
            except:
                logger.info(f"Error in replying or already replied to {mention.id}")

    put_last_tweet(file, new_id)
