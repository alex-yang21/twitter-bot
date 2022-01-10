from flask import Flask
import tweet_reply

import atexit
from apscheduler.schedulers.background import BackgroundScheduler


def tweet_replies():
    tweet_reply.respondToTweet("tweet_id.txt")

def daily_quote():
    tweet_reply.tweet_quote()

def check_dms():
    tweet_reply.reply_dms("dm_id.txt")


scheduler = BackgroundScheduler()
scheduler.add_job(func=tweet_replies, trigger="interval", seconds=180)
scheduler.add_job(func=daily_quote, trigger="interval", seconds=86400)
scheduler.add_job(func=check_dms, trigger="interval", seconds=300)

scheduler.start()

application = Flask(__name__)


@application.route("/")
def index():
    return "Follow @jarjarbot1!"

atexit.register(lambda: scheduler.shutdown())

if __name__ == "__main__":
    application.run(port=5000, debug=True)
