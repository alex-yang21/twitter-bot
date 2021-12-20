import tweepy
import credentials

api_key = credentials.api_key
api_key_secret = credentials.api_key_secret
access_token = credentials.access_token
access_token_secret = credentials.access_token_secret

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

def test():
    pass
