# Gungan Translator Twitter Bot with [Tweepy](https://docs.tweepy.org/en/stable/api.html)

### Follow us on Twitter [@jarjarbot1](https://twitter.com/jarjarbot1)! Support us on [Ko-fi](https://ko-fi.com/jarjarbot1)!

### Translation
Custom translator is built and explained in the `translation` directory. Translation is typically a 1-1 mapping but also uses the [`SpaCy`](https://spacy.io/usage/linguistic-features) NLP package for noun/verb detection and syllable counting, which is useful for other aspects of translation.

### User Replies
Twitter users can tag the bot in reply to a tweet, and the bot will translate the original tweets text and reply tweet.

![Screen Shot 2022-01-11 at 2 44 42 AM](https://user-images.githubusercontent.com/57927187/148928594-be2e72ef-1f1b-4d4e-a9ee-ac327f792462.png)

### User DMs
Users can direct message the bot tweets, which the bot will translate and quote retweet the original tweet if it follows the user. Otherwise the bot will only reply to the original tweet with the translation. The bot will then direct message the translated tweet back to the original sender.

![Screen Shot 2022-01-11 at 2 46 46 AM](https://user-images.githubusercontent.com/57927187/148928831-aae5a367-570c-44a5-a3d1-10b9257390fb.png)

See `tweets` directory for more information.

### Query Tweets
Some tweets with certain key words will be translated, using twitter's `search_tweets` API. Currently our query is 'jar jar binks' and runs twice a day.

### Disclaimer
Anyone can direct message or tag this bot, and as such, there may be material deemed inappropriate to some twitter users. Translations are not endorsements, and there are some safeguards to prevent from offensive or hateful language. Preventing misinformation or other inappropriate uses will be monitored by admins, but some tweets may regrettably slip through the cracks.

### Resources
Credit to: https://auth0.com/blog/how-to-make-a-twitter-bot-in-python-using-tweepy/

Gungan information from: https://starwars.fandom.com/wiki/Gungan_Basic
