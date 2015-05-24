import urllib2
import json
import cgi
import cgitb

cgitb.enable()

class City :
    def __init__(self,Name,Tags,Points) :
        self.Points = Points
        self.Name = Name
        self.Tags = Tags

class Result :
    def __init__(self,Name,Points,Price,Outgoing,Returning,url):
        self.Name = Name
        self.Points = Points
        self.Price = Price
        self.Outgoing = Outgoing
        self.Returning = Returning
        self.url = url

Ranked = ["","",""]
def rankCities(listOfCities, listofactivities, startdate, enddate):
    for city in listOfCities :
        apikey = '&apikey=j3HAAFcwQG6n3X1Q0Ec84wgwZuDmwiFY'
        url = 'http://terminal2.expedia.com:80/x/activities/search?'
        url = url+'&location=' + str(city.Name)
        if(startdate):
            url = url + '&startDate'+startdate
            if(enddate):
                url = url+'&endDate'+enddate
	url = url + apikey
        response = urllib2.urlopen(url).read()
	data = json.loads(response)
	for activity in listofactivities:
	    try:
                city.Points = city.Points + data['filterCategories'][activity]['count']
	    except:
	       continue
    sorted(listOfCities, key=lambda city: city.Points, reverse=True)
    for i in range(3):
        Ranked[i] = listOfCities[i]
        print Ranked[i]
    return Ranked

Cities = []
Results = []

Destination = ["Berlin","London","Montreal","Dubai","Phuket"]
BerTags =["City","Big","Historical", "Sausage", "CurryWurst","NightLife","German","Brandenburg","Reichstag","Germany"]
LonTags =["City","Big","Historical","Rain", "Fish'nChips","Nightlife","English","Pubs","Big Ben","England"]
MonTags =["City","Big","Historical","Poutine","Frostbite","Nightlife","Ski","McGill","Quebec"]
DubTags =["City","Big","Modern","Beach","Sun","Hot","Burj Khalifa"]
PhuTags =["City","Sun","Beach","Nightlife","Thailand"]
TagList =[BerTags,LonTags,MonTags,DubTags,PhuTags]

form = cgi.FieldStorage()
BegDate = "2015-06-10"
EndDate = "2015-06-12"
CatChoice = ""
RequestTags = ["City"]
RequestActivities = ["Nightlife"]
Departure = "Montreal"
if "startDate" in form:
    Begdate=form["startDate"].value
    if(form["EndDate"].value) :   
        EndDate=form["EndDate"].value
if "Type of Trip" in form :
    CatChoice = form["Type of trip"].value
if "Tags" in form : 
    RequestTags = form["Tags"].value
if "Activities" in form :
    RequestActivities = form["Activities"].value
if "Departure" in form:
    Departure = form["Departure"].value

    
for i in range(len(Destination)) :
    if Destination[i] == Departure :
        continue
    city = City(Destination[i],TagList[i], 0)
    Cities.append(city)


form = cgi.FieldStorage()
BegDate = "2015-06-10"
EndDate = "2015-06-12"
CatChoice = ""
RequestTags = ["City"]
RequestActivities = ["Nightlife"]
Departure = "Montreal"
if "startDate" in form:
    Begdate=form["startDate"].value
    if(form["EndDate"].value) :   
        EndDate=form["EndDate"].value
if "Type of Trip" in form :
    CatChoice = form["Type of trip"].value
if "Tags" in form : 
    RequestTags = form["Tags"].value
if "Activities" in form :
    RequestActivities = form["Activities"].value
if "Departure" in form:
    Departure = form["Departure"].value


NarrowDest =[]
for i in range(len(RequestTags)):
    for j in range(len(Cities)):
        for k in range(len(Cities[j].Tags)):
            if RequestTags[i] == Cities[j].Tags[k]:
                NarrowDest.append(Cities[j])

RankedList = rankCities(NarrowDest, RequestActivities, BegDate, EndDate)

for city in RankedList :
    DepCity = Departure.lower()
    ArrCity = city.Name.lower()
    DepCity.replace(" ", "%20")
    ArrCity.replace(" ", "%20")

    DepUrl = "http://terminal2.expedia.com/x/suggestions/regions?query="+DepCity+"&apikey=bWi3OmhFA3L34BLYkjYsucA6SVmMU8lr"
    response = urllib2.urlopen(DepUrl).read()
    data = json.loads(response)
    DepAir = data["sr"][0]["a"]
    
    ArrUrl = "http://terminal2.expedia.com/x/suggestions/regions?query="+ArrCity+"&apikey=bWi3OmhFA3L34BLYkjYsucA6SVmMU8lr"
    response = urllib2.urlopen(ArrUrl).read()
    data = json.loads(response)
    ArrID = data['sr'][0]['id']
    ArrAir = data['sr'][0]['a']

    PackageUrl = "http://terminal2.expedia.com:80/x/packages?originAirport="+DepAir+"&destinationAirport="+ArrAir+"&departureDate="+BegDate+"&returnDate="+EndDate+"&regionid="+ArrID+"&limit=1&apikey=bWi3OmhFA3L34BLYkjYsucA6SVmMU8lr"
    response = urllib2.urlopen(PackageUrl).read()
    data = json.loads(response)
    DepTravelTime =data["FlightList"]["Flight"]["FlightItinerary"]["FlightLeg"][0]["FlightDuration"]
    RetTravelTime =data["FlightList"]["Flight"]["FlightItinerary"]["FlightLeg"][1]["FlightDuration"]
    Price = str(data["PackageSearchResultList"]["PackageSearchResult"]["PackagePrice"]["TotalPrice"]["Value"])+" "+data["PackageSearchResultList"]["PackageSearchResult"]["PackagePrice"]["TotalPrice"]["Currency"]
    ResultUrl = data["PackageSearchResultList"]["PackageSearchResult"]["DetailsUrl"]

    
    DepTravelTime = DepTravelTime.replace("PT","").replace("H"," hours and ").replace("M"," minutes") 
    RetTravelTime = RetTravelTime.replace("PT","").replace("H"," hours and ").replace("M"," minutes") 
    result = Result(city.Name,city.Points,Price,DepTravelTime,RetTravelTime,ResultUrl)
    Results.append(result)
    length = len(Results)

print ''' Content type: Text\n\n

<html>
<header>
<title>Your %d Travel</title>
<body>'''% length
for city in Results :
    print city.Name + "<br>"
print '''</body>
</html>'''





    
