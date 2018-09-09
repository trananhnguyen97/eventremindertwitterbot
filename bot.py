import tweepy
import auth

#create a class inherithing from the tweepy  StreamListener
class BotStreamer(tweepy.StreamListener):

    # Called when a new status arrives which is passed down from the on_data method of the StreamListener
    def on_status(self, status):
        username = status.user.screen_name
        status_id = status.id

    def on_status(self, status):
        print ("This is the retweet")
        auth.api.update_status('@' + status.author.screen_name + ' '+'My status update', status.id)


myStreamListener = BotStreamer()

#Construct the Stream instance
stream = tweepy.Stream(auth.auth, myStreamListener)
stream.filter(track=['@uofuevent'])
