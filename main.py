import tweepy
import auth
import re
import json
import database

#create a class inherithing from the tweepy  StreamListener
class BotStreamer(tweepy.StreamListener):

    def on_status(self, status):

        # Tweeter info
        username = status.user.screen_name
        status_id = status.id

        # Accept event information with #postuofuevent
        content = status.text

        event_today = database.event_list_today
        event_today_name = []

        # Posting events
        if (bool(re.search("#posteventuofu", content))):
            auth.api.update_status('@' + username + ' ' + 'Event posting request accepted', status_id)

        # Getting events category
        if (bool(re.search("#geteventuofu", content))):
            category = []
            date = []

            for event in event_today:
                # Academic events
                if (bool(re.search("#academic", content))):
                    category.append("#academic ")
                    if event.eventCategory == "academic":
                        event_today_name.append("#"+event.eventName+" ")

                if (bool(re.search("#athletic", content))):
                    category.append("#athletic ")
                    if event.eventCategory == "athletic":
                        event_today_name.append("#"+event.eventName+" ")

                if (bool(re.search("#hobby", content))):
                    category.append("#hobby ")
                    if event.eventCategory == "hobby":
                        event_today_name.append("#"+event.eventName+" ")

                if (bool(re.search("#other", content))):
                    category.append("#other ")
                    if event.eventCategory == "other":
                        event_today_name.append("#"+event.eventName+" ")

            # Getting events date
            if (bool(re.search("#today", content))):
                date.append("#today ")

            if (bool(re.search("#tomorrow", content))):
                date.append("#tomorrow ")

            category_str = ''.join(category)
            date_str = ''.join(date)

            event_today_name_str = ''.join(event_today_name)

            print(event_today_name_str)

            auth.api.update_status('@' + username + ' #today ' + 'event ' + date_str + '- ' + event_today_name_str, status_id)


myStreamListener = BotStreamer()

#Construct the Stream instance
stream = tweepy.Stream(auth.auth, myStreamListener)
stream.filter(track=['@uofuevent'])
