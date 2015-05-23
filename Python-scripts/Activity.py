import urllib2
import json
from pprint import pprint

url = 'http://terminal2.expedia.com/x/activities/search?location=Paris&startDate=2015-08-10&apikey=bWi3OmhFA3L34BLYkjYsucA6SVmMU8lr'

response = urllib2.urlopen(url);
data = json.load(response)

class Activity :
    def __init__(self,name,categories, price, customertype, duration, cancel,urlimg):
        self.name = name
        self.categories = categories
        self.price = price
        self.customertype = customertype
        self.duration = duration
        self.cancel = cancel
        self.img = urlimg

          

city = data["destination"]
area = data["fullName"]
numberint = (data["total"])
numberstr = str(numberint)



print "Here are the " + numberstr + " activities in " + area
print "\n"
activities =[]
for i in range(numberint) :
    name = data["activities"][i]["title"]
    categories = str(data["activities"][i]["categories"])
    categories = categories.replace("u'","").replace("[",'').replace("]","").replace("'","")
    price = data["activities"][i]["fromPrice"]
    customertype = data["activities"][i]["fromPriceLabel"]
    duration = data["activities"][i]["duration"]
    cancel = data["activities"][i]["freeCancellation"]
    urlimg = data["activities"][i]["imageUrl"]
    activity = Activity(name, categories, price, customertype, duration, cancel, urlimg)
    activities.append(activity)
     
    print activities[0].name
    print categories
    print "Starting from "+ price+ " per " + customertype
    print "Duration :" + duration
    if not (cancel) :
            print "Cancelling is subject to fees"
    print "Free cancellation is possible"        
    print "\n"
