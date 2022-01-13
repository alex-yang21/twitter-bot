from tweet_reply import put_last_tweet

from app import api
from app import logger

from translator import get_translation
from translation.banned_words import is_profane

def get_tweet_text(dm):
    """
    Gets tweet text from a direct message.
    """
    return dm._json["message_create"]["message_data"]["text"]

def get_tweet_id_url(dm):
    """
    Gets tweet id and url from a direct message if a tweet is sent. Else return None.
    """
    dm_data = dm._json["message_create"]["message_data"]
    urls = dm_data["entities"]["urls"]
    if urls:
        url = urls[0]["expanded_url"]
        url_arr = url.split("/")
        return (url_arr[-1], url)

def get_last_dm(file):
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


def reply_dms(file):
    """
    Checks for direct messages of tweets to respond to with translations.
    Stores most recently fulfilled dm id in file and writes to with newest one.
    """
    last_id = get_last_dm(file)
    if last_id == 1:
        logger.info("No dms yet")
        return

    dms = api.get_direct_messages(count=20) # don't anticipate doing more than 20 dms per day

    dm_id, tweet_id = 0, 0
    flag = False
    for dm in reversed(dms): # start with oldest dm first
        text = get_tweet_text(dm)
        dm_id = int(dm.id)
        sender_id = dm._json["message_create"]["sender_id"]
        logger.info(f"Checking dm from sender: {sender_id}. dm_id: {dm_id}, tweet text: {text}")

        pair = get_tweet_id_url(dm)
        if not pair:
            logger.info("DM had no associated tweet")
            continue
        tweet_id, url = pair
        logger.info(f"Attempting to tweet with tweet id: {tweet_id} and url: {url}")

        if dm_id > last_id: # checks if any new DMs
            logger.info("someone dmed me...")
            logger.info(f"Replying back to {dm_id}")
            tweet = None
            try:
                logger.info("Finding tweet")
                tweet = api.get_status(id=tweet_id, tweet_mode="extended")
                screen_name = tweet.user._json["screen_name"]
                logger.info(f"Translating tweet: {tweet.full_text}")
                logger.info("Checking for profanity")
                if is_profane(tweet.full_text):
                    logger.info(f"Found profanity: {word}")
                    assert 1 == 2 # fail the try block
                translation = get_translation(tweet.full_text)
                logger.info(f"Translated tweet: {translation}")
                logger.info("Tweeting translation")
                translated_tweet = api.update_status(status=translation, attachment_url=url)
                logger.info(f"Sending translated tweet to original sender: {sender_id}")
                formatted_url = f"https://twitter.com/{screen_name}/status/{translated_tweet.id}"
                new_dm = api.send_direct_message(recipient_id=sender_id, text=formatted_url)
                dm_id = new_dm.id
                flag = True
            except:
                logger.info(f"Error in replying or already replied to {dm_id}")

    if flag:
        put_last_tweet(file, dm_id)
    else:
        logger.info("No new dms found")
