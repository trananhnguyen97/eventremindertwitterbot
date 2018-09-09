import eventClass
import tweepy
import auth

api1 = tweepy.API(auth.auth)
print(api1.direct_messages(count=1)[0].text)