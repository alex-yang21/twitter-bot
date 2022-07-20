import re

from tweet_reply import put_last_tweet
from app import api
from app import logger

from translator import get_translation, get_partitions
from translation.banned_words import is_profane

alex_id = "2680442773" # we now only let DMs be full tweets if I send them, no longer just if the account is following

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

def following(sender_id):
    logger.info(f"Checking if we follow user with id: {sender_id}")
    sender_id = [sender_id]
    relationship = api.lookup_friendships(user_id=sender_id)[0]
    return relationship.is_following

def reply_dms(file):
    """
    Checks for direct messages of tweets to respond to with translations.
    Stores most recently fulfilled dm id in file and writes to with newest one.
    """
    last_id = get_last_dm(file)
    if last_id == 1:
        logger.info("No dms yet")
        return

    dms = api.get_direct_messages(count=15) # don't anticipate doing more than 10 dms per cycle

    dm_id, tweet_id = 0, 0
    flag = False
    for dm in reversed(dms): # start with oldest dm first
        status = 0

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
            flag = True
            logger.info("someone dmed me...")
            logger.info(f"Replying back to dm with id: {dm_id}")
            tweet = None
            try:
                logger.info("Finding tweet")
                tweet = api.get_status(id=tweet_id, tweet_mode="extended")
                logger.info(f"Translating tweet: {tweet.full_text}")

                # check that the tweet is in English
                if tweet.lang != "en":
                    status = 1
                    logger.info("Tweet is not in english. Do not translate.")
                    api.send_direct_message(recipient_id=sender_id, text="Automated message: sorry tweet cannot be translated because it may not be in English. Only English is supported!")
                    assert 1 == 2 # fail the try block

                # check if we are translating our own tweet
                screen_name = tweet.user.screen_name
                if screen_name == "jarjarbot1":
                    status = 2
                    logger.info("Do not translate our own tweets!")
                    api.send_direct_message(recipient_id=sender_id, text="Automated message: sorry I can't translate my own tweets!")
                    assert 1 == 2 # fail the try block

                # check for profanity
                logger.info("Checking for profanity")
                if is_profane(tweet.full_text):
                    status = 3
                    logger.info("Found profanity. Do not translate.")
                    api.send_direct_message(recipient_id=sender_id, text="Automated message: sorry tweet cannot be translated because it may contain profanity or a sensitive topic.")
                    assert 1 == 2 # fail the try block

                # truncate the tweet text to be below 280 character limit if possible
                truncated = re.sub(r' https://t.co/\w{10}', '', tweet.full_text) # replace annoying url at end
                truncated = re.sub(' +', ' ', truncated) # replace all unnecessary white space

                # if the translation is longer than 280 characters split into two tweets
                translation = get_translation(truncated)
                logger.info(f"Translated tweet: {translation}")

                translated_tweet = None
                # is_following = following(sender_id) -- deprecated
                is_alex = sender_id == alex_id
                if len(translation) > 280 or (not is_alex and len(translation) + len(screen_name) + 2 > 280):
                    logger.info("Translation longer than 280 characters, breaking into two tweets")

                    first, second = get_partitions(translation)
                    # if the sender is me, we tweet the translation as a quote retweet, if not a reply
                    if is_alex:
                        logger.info(f"Quote tweeting first part: {first}")
                        translated_tweet = api.update_status(status=first, attachment_url=url)
                        logger.info(f"Replying with second part: {second}")
                        api.update_status(status=second, in_reply_to_status_id=translated_tweet.id)
                    else:
                        logger.info(f"Replying with first part: {first}")
                        translated_tweet = api.update_status(status=first, in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
                        logger.info(f"Replying with second part: {second}")
                        api.update_status(status=second, in_reply_to_status_id=translated_tweet.id, auto_populate_reply_metadata=True)
                else:
                    # if the sender is me, we tweet the translation as a quote retweet, if not a reply
                    if is_alex:
                        logger.info("Quote tweeting translation")
                        translated_tweet = api.update_status(status=translation, attachment_url=url)
                    else:
                        logger.info("Replying with translation")
                        translated_tweet = api.update_status(status=translation, in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)

                logger.info(f"Sending translated tweet to original sender: {sender_id}")
                formatted_url = f"https://twitter.com/jarjarbot1/status/{translated_tweet.id}"
                new_dm = api.send_direct_message(recipient_id=sender_id, text=formatted_url)
                dm_id = new_dm.id
                put_last_tweet(file, dm_id)
                status = 4 # success
            except:
                put_last_tweet(file, dm_id)
                logger.info(f"DM: Error in replying or already replied to {dm_id}")

            if status == 0: # unknown failure occurred, attempt to DM
                try:
                    api.send_direct_message(recipient_id=sender_id, text="Automated message: sorry for some reason I can't translate the tweet you sent me")
                except:
                    pass

    if not flag:
        logger.info("No new dms found")
