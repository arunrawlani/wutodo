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


if "departure" in form:
    BegDate = form["departure"].value
    if "return" in form:
        EndDate = form["return"].value


