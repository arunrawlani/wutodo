import cgi
from random import randint 


Destination = ["Berlin","London","Montreal","Dubai","Phuket","Paris","Bali"]

form = cgi.FieldStorage()
BegDate = "2015-06-10"
EndDate = "2015-06-12"
CatChoice = ""
RequestTags = ["Quebec"]
RequestActivities = ["Adventures","Food & Drink"]
DepIndex = randint(0,6)
Departure = Destination[Index]
ArrIndex = DepIndex
while DepIndex == ArrIndex :
    ArrIndex = randint
Arrival = Destination[Arrindex]


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

