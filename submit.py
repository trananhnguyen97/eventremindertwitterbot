import eventClass
import tweepy
import auth
import database

api1 = tweepy.API(auth.auth)
#print(api1.direct_messages(count=100)[0].text)
#print(api1.direct_messages(count=100, since_id=0)[1].text)
numDM = len(api1.direct_messages())
print("Number of DMs: ", numDM)

###print(api1.direct_messages(count=200)[i].sender_screen_name)

def checkDM():
    for i in range (database.lastID, numDM):
        author=api1.direct_messages(count=200)[i].sender_screen_name
        print(api1.direct_messages(count=200)[i].text)
        dm=api1.direct_messages(count=200)[i].text
        print ("Current DM: ", dm)
        tweetID=api1.direct_messages(count=200)[i].id
        if (dm.find("EVENT: ")==0):
            postTweet(addEvent(i))
            api1.destroy_direct_message(tweetID)
        elif (dm.find("INFO: ")==0):
            info(i)
            api1.destroy_direct_message(tweetID)
        else:
            text = "Try again"
            api1.send_direct_message(screen_name=author,text=text)
            api1.destroy_direct_message(tweetID)

def info(x=0):
    dm=api1.direct_messages(count=200)[x].text
    if not (dm.find("INFO: ")==-1):
        if not (dm.find("NAME: ")==-1):
            nameStr = dm.find("NAME: ")
            eventList = database.nameLookup(dm[nameStr+len("NAME: "):])
            tweetText="";
            for x in range(0, len(eventList)):
                tweetText += "#" + eventList[x].eventName

        elif not (dm.find("DATE: ")==-1):
            dateStr = dm.find("DATE: ")
            database.dateLookup(dm[dateStr+len("DATE: "):])
        elif not (dm.find("CAT: ")==-1):
            catStr = dm.find("CAT: ")
            database.catLookup(dm[catStr+len("CAT: "):])
        else:
            return False



def addEvent(x=0):
    dm=api1.direct_messages(count=200)[x].text
    print(dm)
    if not (dm.find("EVENT: ")==-1 or dm.find("DATE: ")==-1 or dm.find("DESC: ")==-1 or dm.find("WEB: ")==-1 or dm.find("CATE: ")==-1 or dm.find("FOOD: ")==-1):
        eventStr = dm.find("EVENT: ")
        dateStr = dm.find("DATE: ")
        descStr = dm.find("DESC: ")
        webStr = dm.find("WEB: ")
        catStr = dm.find("CATE: ")
        foodStr = dm.find("FOOD: ")
        #print (eventStr, dateStr, descStr, webStr, catStr, foodStr)
        newEvent = eventClass.Event(eventName=dm[eventStr+len("EVENT: "):dateStr-2], eventDate=dm[dateStr+len("DATE: "):descStr-2], eventDesc=dm[descStr+len("DESC: "):webStr-2], eventWeb=dm[webStr+len("WEB: "):catStr-2], eventCategory=dm[catStr+len("CATE: "):foodStr-2], eventFood=dm[foodStr+len("FOOD: "):])
        #print(newEvent.eventName)
        return newEvent
    else:
        api1.send_direct_message(api1.direct_messages(count=200)[x].sender_screen_name, "Please reformat your request")
        #destroy dm
        return False


def postTweet(event):
    tweetText = "Hey everyone, " + event.eventName + " is an upcoming event on " + event.eventDate + ". Here's the description: " + event.eventDesc + ", and here is the event's website: " + event.eventWeb + " Food status: " + event.eventFood + " #" + event.eventCategory + "Event"
    api1.update_status(tweetText)

checkDM()