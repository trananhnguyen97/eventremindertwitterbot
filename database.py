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


def nameLookup(name):
    return_list = []
    for x in listofevents:
        if name == x.eventName:
            return_list.append(x)
    return return_list

#
def dateLookup(date):
    return_list = []
    for x in listofevents:
        if date == x.eventDate:
            return_list.append(x)
    return return_list


def catLookup(category):
    return_list = []
    for x in listofevents:
        if category == x.eventCategory:
            return_list.append(x)
    return return_list


def is_there_something_to_post_today():
    list_months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    today_date = list_months[(now.month)]+ " " + str(now.day)
    next_weeks_day = now.day + 7
    next_week_date = list_months[(now.month)] + " " + str(next_weeks_day)
    #
    for x in listofevents:
        if today_date == x.eventDate:
            event_list_today.append(x)
        if next_week_date == x.eventDate:
            event_list_today.append(x)


def read_from_file():
    f = open("events.txt", 'r')

    # text_line = f.readline()
    # print(text_line)
    for line in f:
        x = line.split(', ', 6)
        create_event(x[0], x[1], x[2], x[3], x[4], x[5])
    f.close()



def write_to_file():
   f = open("events.txt", "w")
   for line in listofevents:
       f.write(line.eventName + ", " + line.eventDate + ", " + line.eventDesc + ", " + line.eventWeb + ", " + line.eventCategory + ", " + line.eventFood+"\n")
   f.close()


create_event("Football Training", "September 9", "DESCRIPTION", "WEBADRESS", "CATEGORY", "FOOD YES")
create_event("Sports Workshop", "September 16", "DESCRIPTION", "WEBADRESS", "CATEGORY", "FOOD NO")
create_event("Free Food", "September 9", "Come get free food", "WEBADRESS", "CATEGORY", "FOOD YES")


#write_to_file()
read_from_file()

# if search_for_duplicate("NAME"):
#     print("There was a duplicate")


# for x in catLookup("CATEGORY"):
#     print(x.eventCategory)
is_there_something_to_post_today()