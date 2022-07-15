import re

from app import api
from app import logger

from translation.translator import get_translation, get_partitions
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
    logger.info("Updated the file with the latest tweet id")

def recursion_check(screen_name, text):
    """
    We want to prevent recursive translation calls.

    One case is when a user attempts to translate a tweet from @jarjarbot1 and spams "translate".

    There is another small edge case where another user replies to the original user tweet '@jarjarbot1 translate'
    with the word 'translate' in their reply. Ex: "translate deez nuts".

    To prevent these, we check that the tweet author is not @jarjarbot1, and check to see if the tweet text is purely the word 'translate' once all mentions are removed.
    This is not exhaustive but should handle most cases.

    Returns TRUE if the tweet we are translating is a translate request itself, in which case we do not translate that tweet.
    """
    # check if we are translating our own tweet
    if screen_name == "jarjarbot1":
        return True

    # check if the tweet we are translating is a translation request
    text_arr = text.split()
    words = []
    for word in text_arr:
        if word[0] != '@':
            words.append(word)
    return words == ["translate"]

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

        if keyword in mention.text.lower(): # check for chosen keyword above
            logger.info(f"Responding back to {mention.id}")
            replied_tweet = None

            try:
                logger.info("Finding parent tweet")
                replied_tweet = api.get_status(id=mention.in_reply_to_status_id, tweet_mode="extended") # grab the tweet that this mention is replying to
                logger.info(f"Translating tweet: {replied_tweet.full_text}")
                
                # check if the tweet we are trying to translate is of form '@jarjarbot1 translate', if so, do not translate
                # or if the tweet we are trying to translate is from @jarjarbot1
                if recursion_check(replied_tweet.user.screen_name, replied_tweet.full_text.lower()):
                    logger.info(f"Tweet is recursive. Do not translate.")
                    assert 1 == 2 # fail try block

                logger.info("Checking for profanity")

                if is_profane(replied_tweet.full_text):
                    logger.info("Found profanity")
                    # logger.info("Replying to tweet saying I can't translate")
                    # api.update_status(status="@" + mention.user.screen_name + " Sorry I can't translate this :(", in_reply_to_status_id=mention.id)
                    put_last_tweet(file, new_id)
                    assert 1 == 2 # fail the try block

                # truncate the tweet text to be below 280 character limit if possible
                truncated = re.sub(r' https://t.co/\w{10}', '', replied_tweet.full_text) # replace annoying url at end
                truncated = re.sub(' +', ' ', truncated) # replace all unnecessary white space
                translation = get_translation(truncated)
                logger.info(f"Translated tweet: {translation}")

                translated_tweet = None
                if len(translation) > 280 - len(mention.user.screen_name) - 2:
                    logger.info("Translation longer than 280 characters")
                    first, second = get_partitions(translation)
                    logger.info(f"Replying with first part: {first}")
                    translated_tweet = api.update_status(status="@" + mention.user.screen_name + " " + first, in_reply_to_status_id=mention.id)
                    logger.info(f"Replying with second part: {second}")
                    api.update_status(status=second, in_reply_to_status_id=translated_tweet.id)
                else:
                    logger.info("Replying to tweet")
                    api.update_status(status="@" + mention.user.screen_name + " " + translation, in_reply_to_status_id=mention.id)
            except:
                api.send_direct_message(recipient_id=mention.user.id, text="Automated message: sorry for some reason I can't translate the tweet you tagged me in :(")
                logger.info(f"Error in replying or already replied to {mention.id}")

    put_last_tweet(file, new_id)
