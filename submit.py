import eventClass
import tweepy
import auth
import database

api1 = tweepy.API(auth.auth)
#print(api1.direct_messages(count=100)[0].text)
#print(api1.direct_messages(count=100, since_id=0)[1].text)
numDM = len(api1.direct_messages())
#print("Number of DMs: ", numDM)


def addEvent():
    for i in range(0, numDM):
        dm=api1.direct_messages(count=200)[i].text
        if not (dm.find("EVENT: ")==-1 or dm.find("DATE: ")==-1 or dm.find("DESC: ")==-1 or dm.find("WEB: ")==-1 or dm.find("CATE: ")==-1 or dm.find("FOOD: ")==-1):
            eventStr = dm.find("EVENT: ")
            dateStr = dm.find("DATE: ")
            descStr = dm.find("DESC: ")
            webStr = dm.find("WEB: ")
            catStr = dm.find("CATE: ")
            foodStr = dm.find("FOOD: ")
            print (eventStr, dateStr, descStr, webStr, catStr, foodStr)
            newEvent = eventClass.Event(eventName=dm[eventStr+len("EVENT: "):dateStr-2], eventDate=dm[dateStr+len("DATE: "):descStr-2], eventDesc=dm[descStr+len("DESC: "):webStr-2], eventWeb=dm[webStr+len("WEB: "):catStr-2], eventCategory=dm[catStr+len("CATE: "):foodStr-2], eventFood=dm[foodStr+len("FOOD: "):])
            print(newEvent.eventName)
            return newEvent


def postTweet(event):
    tweetText = "Hey everyone, " + event.eventName + " is an upcoming event on " + event.eventDate + ". Here's the description: " + event.eventDesc + ", and here is the event's website: " + event.eventWeb + " Food status: " + event.eventFood + " #" + event.eventCategory + "Event"
    api1.update_status(tweetText)


postTweet(addEvent())

# database.create_event("NOTNAME", "September 9", "DESCRIPTION", "WEBADRESS", "CATEGORY", "FOOD YES")
# database.create_event("NAME", "September 9", "DESCRIPTION", "WEBADRESS", "CATEGORY", "FOOD YES")

# if database.search_for_duplicate("NAME"):
#     print("THERE IS A DUPLICATE")

# database.is_there_something_to_post_today()
# for x in database.event_list_today:
#     print(x.eventName)

