from flask import Flask
import tweet_reply

import atexit
from apscheduler.schedulers.background import BackgroundScheduler


def tweet_replies():
    tweet_reply.respondToTweet('tweet_id.txt')
    print("Success")

def daily_quote():
    tweet_reply.tweet_quote()


scheduler = BackgroundScheduler()
scheduler.add_job(func=tweet_replies, trigger="interval", seconds=120)
scheduler.add_job(func=daily_quote, trigger="interval", seconds=86400)
scheduler.start()

application = Flask(__name__)


@application.route("/")
def index():
    return "Follow @jarjarbot1!"

atexit.register(lambda: scheduler.shutdown())

if __name__ == "__main__":
    application.run(port=5000, debug=True)
