import webbrowser
#import beautifulsoup
#Use beautifulSoup to parse the webpages HTML
import requests
from lxml import html
#Use request to jump from webpage to webpage

page = requests.get('https://www.utah.edu/events/')
tree = html.fromstring(page.content)

itemVar = tree.xpath('//span[@class="twDetailTime"]/text()')
# //span[@class="twDetailTime"]/text()

print(itemVar) 
#
# page = requests.get("https://www.trumba.com/calendars/university-of-utah.rss")
# #prints webpages HTML
#
# print(page.content)
# # f = open('HoldsRss', 'w')
# # #page.content.ToString()
# # f.write(page.text)
# # f.close()