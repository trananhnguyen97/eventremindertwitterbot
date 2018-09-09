import tweepy
import auth
import re

#create a class inherithing from the tweepy  StreamListener
class BotStreamer(tweepy.StreamListener):

    # Called when a new status arrives which is passed down from the on_data method of the StreamListener
    def on_status(self, status):
        username = status.user.screen_name
        status_id = status.id

    def on_status(self, status):

        # Accept event information with #postuofuevent
        content = status.text
        if (bool(re.search("#posteventuofu", content))):
            auth.api.update_status('@' + status.author.screen_name + ' ' + 'Event posting request accepted', status.id)
        if(bool(re.search("#geteventuofu", content))):
            auth.api.update_status('@' + status.author.screen_name + ' ' + 'Information about event: ', status.id)


myStreamListener = BotStreamer()

#Construct the Stream instance
stream = tweepy.Stream(auth.auth, myStreamListener)
stream.filter(track=['@uofuevent'])
