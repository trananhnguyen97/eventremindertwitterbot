import datetime
#currentid (integer)
import eventClass

listofevents = []

def create_event(eventName, eventDate, eventDesc, eventWeb, eventCategory, eventFood):
    listofevents.append(eventClass(eventName, eventDate, eventDesc, eventWeb, eventCategory, eventFood))

def search_for_duplicate(name):
    for x in listofevents:
        if name == listofevents.index(x).eventName:
            return False
        else:
            return True

def