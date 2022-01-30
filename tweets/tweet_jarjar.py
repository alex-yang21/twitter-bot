import re

from app import api
from app import logger

from translation.translator import get_translation
from translation.banned_words import is_profane
from tweets.tweet_reply import get_last_tweet, put_last_tweet

bot_accounts = {
    "jarjarbot1",
    "starwars_facts",
    "Yoda_Bot",
    "controverSW",
    "SWTheoriesBot",
    "SWSCRIPTBOT",
    "whyshipreylo",
    "StarClickBait",
    "TalkLikeJarJar",
    "StarWarsInforms",
    "MachineBot",
    "swgaybot"
}

def reply_jarjar(file, query="jar jar binks -filter:retweets"):
    """
    Automatically translates tweets that contain the query 'jar jar binks'.
    """
    last_id = get_last_tweet(file)
    query_tweets = api.search_tweets(q=query, lang="en", result_type="mixed", count=5, tweet_mode="extended", since_id=last_id)

    if len(query_tweets) == 0: # no new tweets to respond to
        logger.info("no tweets with query found")
        return

    logger.info(f"someone said '{query}'...")
    new_id = 0
    for tweet in reversed(query_tweets):
        new_id = tweet.id
        if tweet.user.screen_name not in bot_accounts and not tweet.in_reply_to_status_id and not tweet._json['is_quote_status']: # tweet is not from a bot account and is not a tweet reply or quote tweet
            logger.info(f"Translating tweet with id: {tweet.id}")

            try:
                logger.info(f"Translating tweet: {tweet.full_text}")
                logger.info("Checking for profanity")
                if is_profane(tweet.full_text):
                    assert 1 == 2 # fail the try block

                # truncate the tweet text
                truncated = re.sub(r' https://t.co/\w{10}', '', tweet.full_text) # replace annoying url at end
                truncated = re.sub(' +', ' ', truncated) # replace all unnecessary white space
                translation = get_translation(truncated)
                logger.info(f"Translated tweet: {translation}")

                if len(translation) > 280:
                    logger.info("Translation longer than 280 characters, don't translate")
                    return
                else:
                    logger.info("Replying to tweet with translation")
                    api.update_status(status="@" + tweet.user.screen_name + " " + translation, in_reply_to_status_id=tweet.id)
            except:
                logger.info(f"Error in replying or already replied to {tweet.id}")

    put_last_tweet(file, new_id)
