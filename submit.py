import eventClass
import tweepy
import auth

api1 = tweepy.API(auth.auth)
print(api1.direct_messages(count=100)[0].text)
print(api1.direct_messages(count=100, since_id=0)[1].text)
numDM = len(api1.direct_messages())
print("Number of DMs: ", numDM)

for i in range(0, numDM):
    dm=api1.direct_messages(count=200)[i].text
    if not (dm.lower().find("event")==-1):
        print(dm)