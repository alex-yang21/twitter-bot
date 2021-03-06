from flask import Flask
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
import tweepy
import logging

import sys
import os
sys.path.append("tweets")
sys.path.append("translation")

# Authenticate to Twitter
api_key = os.environ["API_KEY"]
api_key_secret = os.environ["API_KEY_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# For adding logs in application
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
logger.setLevel(logging.INFO)

from tweet_reply import respond_to_tweet
from tweet_dm import reply_dms
from tweet_jarjar import reply_jarjar

# background scheduling of jobs
def check_replies():
    respond_to_tweet("text_files/tweet_id.txt")

def check_dms():
    reply_dms("text_files/dm_id.txt")

def check_jarjar():
    reply_jarjar("text_files/tweet_jarjar.txt")


scheduler = BackgroundScheduler()
scheduler.add_job(func=check_replies, trigger="interval", seconds=120)
scheduler.add_job(func=check_dms, trigger="interval", seconds=300)
# scheduler.add_job(func=check_jarjar, trigger="interval", seconds=43200)
scheduler.start()

app = Flask(__name__)

@app.route("/")
def index():
    return "Follow @jarjarbot1!"

atexit.register(lambda: scheduler.shutdown())

if __name__ == "__main__":
    app.run(port=5000, debug=True)
