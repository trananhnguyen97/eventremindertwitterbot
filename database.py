import datetime
import eventClass

now = datetime.datetime.now()
listofevents = []
event_list_today = []
event_list_within_the_week = []


def create_event(eventName, eventDate, eventDesc, eventWeb, eventCategory, eventFood):
    listofevents.append(eventClass.Event(eventName, eventDate, eventDesc, eventWeb, eventCategory, eventFood))


def search_for_duplicate(name):
    for x in listofevents:
        if name == x.eventName:
            return True
    return False


# def search_for_duplicate(name):
#     for x in listofevents:
#         if name == listofevents.index(x).eventName:
#             listofevents.remove(x)


# def name_Lookup(name):
#     return_list = []
#     for x in listofevents:
#         if name == listofevents.index(x).eventName:
#             return_list.append(listofevents.index(x))
#     return return_list
#
#
# def dateLookup(date):
#     return_list = []
#     for x in listofevents:
#         if date == listofevents.index(x).eventDate:
#             return_list.append(listofevents.index(x))
#     return return_list
#
#
# def catLookup(category):
#     return_list = []
#     for x in listofevents:
#         if category == listofevents.index(x).eventCategory:
#             return_list.append(listofevents.index(x))
#     return return_list


def is_there_something_to_post_today():
    list_months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    today_date = list_months[(now.month)]+ " " + str(now.day)
    next_weeks_day = now.day + 7
    next_week_date = list_months[(now.month)] + " " + str(next_weeks_day)
    #
    for x in listofevents:
        if today_date == x.eventDate:
            event_list_today.append(listofevents.index(x))
        if next_week_date == x.eventDate:
            event_list_today.append(listofevents.index(x))
    #return event_list_today, event_list_within_the_week


# list_today = []
# list_next_week = []
#list_today, list_next_week = is_there_something_to_post_today()


list_months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October","November", "December"]
print(now.month)