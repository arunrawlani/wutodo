import urllib2
import json
import cgi
import cgitb

cgitb.enable()

class City :
    def __init__(self,Name,Family,Sport,Discovery,Party) :
        self.Name = Name 
        self.Family = Family
        self.Sport = Sport
        self.Discovery = Discovery
        self.Party = Party

Cities = []

Familycat = ["Adventures","Attractions","Theme Parks","Private Tours","Water Activities","Cruises & Water Tours"]
Sportcat = ["Show & Sport Tickets","Walking & Bike Tours","Water Activities"]
Discoverycat = ["Cruises & Water Tours","Day Trips & Excursions","Hop-on Hop-off","Multi-Day & Extended Tours","Tours & Sightseeing","Sightseeing Passes"] 
Partycat = ["Food & Drink","Nightlife"]

form = cgi.FieldStorage()
BegDate = ""
EndDate = ""
if "startDate" in form:
    Begdate=form["startDate"].value
    if(form["EndDate"].value) :   
        EndDate=form["EndDate"].value



Destination = ["Berlin","London","Montreal","Dubai","Phuket"]

for i in range(len(Destination)) :
    url = "http://terminal2.expedia.com/x/activities/search?location="+Destination[i]
    if (BegDate) :
        url = url + "&startDate="+BegDate
        if(EndDate) :
            url = url + "&endDate="+EndDate
    url = url +"&apikey=bWi3OmhFA3L34BLYkjYsucA6SVmMU8lr"
    response = urllib2.urlopen(url)
    data = json.load(response)
    Family = 0
    Sport = 0
    Discovery = 0
    Party = 0
    for i in range(len(Familycat)) :
        if Familycat[i] in data["filterCategories"] :
            Family = Family + data["filterCategories"][Familycat[i]]["count"]
    for i in range(len(Sportcat)) :
        if Sportcat[i] in data["filterCategories"] :
            Sport = Sport + data["filterCategories"][Sportcat[i]]["count"]
    for i in range(len(Discoverycat)) :
        if Discoverycat[i] in data["filterCategories"] :
            Discovery = Discovery + data["filterCategories"][Discoverycat[i]]["count"]
    for i in range(len(Partycat)) :
        if Partycat[i] in data["filterCategories"] :
            Party = Party + data["filterCategories"][Partycat[i]]["count"]
    city = City(Destination[i],Family,Sport,Discovery,Party)
    cities.append(city)
