import datetime
#currentid (integer)
import eventClass

now = datetime.datetime.now()
listofevents = []

def create_event(eventName, eventDate, eventDesc, eventWeb, eventCategory, eventFood):
    listofevents.append(eventClass(eventName, eventDate, eventDesc, eventWeb, eventCategory, eventFood))

def search_for_duplicate(name):
    for x in listofevents:
        if name == listofevents.index(x).eventName:
            return False
        else:
            return True

def nameLookup(name):
    return_list = []
    for x in listofevents:
        if name == listofevents.index(x).eventName:
            return_list.append(listofevents.index(x))
    return return_list

def dateLookup(date):
    return_list = []
    for x in listofevents:
        if date == listofevents.index(x).eventDate:
            return_list.append(listofevents.index(x))
    return return_list

def catLookup(category):
    return_list = []
    for x in listofevents:
        if category == listofevents.index(x).eventCategory:
            return_list.append(listofevents.index(x))
    return return_list

def is_there_something_to_post_today():
    event_list_today = []
    event_list_within_the_week = []
    list_months = ["","January","February","March","April","May","June","July","August","September","October","November","December"]
    # January 30
    todays_date = list_months.index(now.month)+ " " + now.day
    day_var = now.day + 7
    next_week_date = list_months.index(now.month)+ " " + now.day
    #
    for x in listofevents:
        if var == listofevents.index(x).eventDate:
            event_list_today.append(listofevents.index(x))
        if var == listofevents.index(x).eventDate:
            event_list_today.append(listofevents.index(x))
    return
#need to convert month ints to June, July...
# need to call is there something to post today after it is made
# need to make a list for the special today and a list of special tomorrow