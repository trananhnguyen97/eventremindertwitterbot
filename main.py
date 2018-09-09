import tweepy
import auth
import re
import json

#create a class inherithing from the tweepy  StreamListener
class BotStreamer(tweepy.StreamListener):

    def on_status(self, status):

        username = status.user.screen_name
        status_id = status.id

        # Accept event information with #postuofuevent
        content = status.text

        # Posting events
        if (bool(re.search("#posteventuofu", content))):
            auth.api.update_status('@' + username + ' ' + 'Event posting request accepted', status_id)

        # Getting events category
        if (bool(re.search("#geteventuofu", content))):
            category = []
            date = []

            # Academic events
            if (bool(re.search("#academic", content))):
                category.append("#academic ")

            if (bool(re.search("#athletic", content))):
                category.append("#athletic ")

            if (bool(re.search("#hobby", content))):
                category.append("#hobby ")

            if (bool(re.search("#other", content))):
                category.append("#other ")

            # Getting events date
            if (bool(re.search("#today", content))):
                date.append("#today ")

            if (bool(re.search("#tomorrow", content))):
                date.append("#tomorrow ")

            category_str = ''.join(category)
            date_str = ''.join(date)

            auth.api.update_status('@' + username + ' ' + category_str + 'event ' + date_str + '- ', status_id)


myStreamListener = BotStreamer()

#Construct the Stream instance
stream = tweepy.Stream(auth.auth, myStreamListener)
stream.filter(track=['@uofuevent'])
