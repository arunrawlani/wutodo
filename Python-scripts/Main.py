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

Cities = []

Destination = ["Berlin","London","Montreal","Dubai","Phuket"]
BerTags =["Big","Historical", "Sausage", "CurryWurst","NightLife","German","Brandenburg","Reichstag","Germany"]
LonTags =["Big","Historical","Rain", "Fish'nChips","Nightlife","English","Pubs","Big Ben","England"]
MonTags =["Big","Historical","Poutine","Frostbite","Nightlife","Ski","McGill","Quebec"]
DubTags =["Big","Modern","Beach","Sun","Hot","Burj Khalifa"]
PhuTags =["Sun","Beach","Nightlife","Thailand"]
TagList =[BerTags,LonTags,MonTags,DubTags,PhuTags]

for i in range(len(Destination)) :
    city = City(Destination[i],TagList[i], 0)
    Cities.append(city)

form = cgi.FieldStorage()
BegDate = ""
EndDate = ""
CatChoice = ""
RequestTags = ["German"]
if "startDate" in form:
    Begdate=form["startDate"].value
    if(form["EndDate"].value) :   
        EndDate=form["EndDate"].value
if "Type of Trip" in form :
    CatChoice = form["Type of trip"].value
if "Tags" in form : 
    RequestTags = form["Tags"].value

NarrowDest =[]
for i in range(len(RequestTags)):
    for j in range(len(Cities)):
        for k in range(len(Cities[j].Tags)):
            print Cities[j].Tags[k]
            
            if RequestTags[i] == Cities[j].Tags[k]:
                
                NarrowDest.append(Cities[j])
        print "\n"

for i in range(len(NarrowDest)) :
    print NarrowDest[i].Name
