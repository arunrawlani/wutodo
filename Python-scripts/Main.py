import urllib2
import json
import cgi
import cgitb

#cgitb.enable()

class City :
    def __init__(self,Name,Tags,Points) :
        self.Points = Points
        self.Name = Name
        self.Tags = Tags


Ranked = []
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
    listOfCities = sorted(listOfCities, key=lambda city: city.Points, reverse=True)


		
    for i in range(min(3,len(listOfCities))):
		Ranked.append(listOfCities[i])


    return Ranked


Results = []
Cities = []
Destination = ["Berlin","London","Montreal","Dubai","Phuket","Paris","Bali"]
BerTags =["City","Big","Historical", "Sausage", "CurryWurst","NightLife","German","Brandenburg","Reichstag","Germany"]
LonTags =["City","Big","Historical","Rain", "Fish'nChips","Nightlife","English","Pubs","Big Ben","England"]
MonTags =["City","Big","Historical","Poutine","Frostbite","Nightlife","Ski","McGill","Quebec"]
DubTags =["City","Big","Modern","Beach","Sun","Hot","Burj Khalifa"]
PhuTags =["City","Sun","Beach","Nightlife","Thailand"]
ParTags =["City","Big","Historical","Eiffel Tower","Baguette","French","White flags"]
BalTags =["Island","Culture","Beach","Summer","Sun","City"]
TagList =[BerTags,LonTags,MonTags,DubTags,PhuTags,ParTags,BalTags]



form = cgi.FieldStorage()
BegDate = "2015-06-10"
EndDate = "2015-06-12"
CatChoice = ""
RequestTags = ["Quebec"]
RequestActivities = ["Adventures","Food & Drink"]
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
    if (Destination[i]==Departure) :
        continue
    city = City(Destination[i], TagList[i],0)
    Cities.append(city)




NarrowDest =[]
for i in range(len(RequestTags)):
    for j in range(len(Cities)):
        for k in range(len(Cities[j].Tags)):
            if RequestTags[i] == Cities[j].Tags[k]:
				NarrowDest.append(Cities[j])
				#print Cities[j].Name
				#print Cities[j].Tags[k]
				
	
for city in NarrowDest:
    print city.Name


RankedList = rankCities(NarrowDest, RequestActivities, BegDate, EndDate)


print ''' Content type: Text\n\n

<html>
<header>
<title>Your Travel</title>
<body>'''
for city in RankedList :
    print city.Name + "<br>"
print '''</body>
</html>'''





    
