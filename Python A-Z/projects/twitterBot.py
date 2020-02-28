import tweepy
import time

#generate and put your own tokens from your twitter developer account
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

user = api.me()
# print(user)
# print(user.name)
# print(user.screen_name)
# print(user.followers_count)

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)

# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     # print(follower.name)
#     if follower.name =='Sarah Gustman':
#         follower.follow()

search_term = 'trump'
no_tweets = 3

for tweet in tweepy.Cursor(api.search, search_term).items(no_tweets):
    try:
        # tweet.favorite()
        tweet.retweet()
        print('i liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break