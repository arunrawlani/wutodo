import urllib2
import json
import cgi
import cgitb

cgitb.enable()


class Result :
    def __init__(self,Name,Price,OutgoingDate,ReturningDate,url,img):
        self.Name = Name
        self.Price = Price
        self.OutgoingDate = OutgoingDate
        self.ReturningDate = ReturningDate
        self.url = url
        self.img = img

BegDate ="2015-06-15"
EndDate ="2015-06-20"
DepCity = "Montreal"
ArrCity = "Jakarta"
DepCity = DepCity.lower()
ArrCity = ArrCity.lower()
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
LowestPrice = str(data["PackageSearchResultList"]["PackageSearchResult"]["PackagePrice"]["TotalPrice"]["Value"])+" "+data["PackageSearchResultList"]["PackageSearchResult"]["PackagePrice"]["TotalPrice"]["Currency"]
ResultUrl = data["PackageSearchResultList"]["PackageSearchResult"]["DetailsUrl"]

DepTravelTime = DepTravelTime.replace("PT","").replace("H"," hours and ").replace("M"," minutes") 
RetTravelTime = RetTravelTime.replace("PT","").replace("H"," hours and ").replace("M"," minutes") 
result = Result(ArrCity.replace("%20"," "),LowestPrice,DepTravelTime,RetTravelTime,ResultUrl)

print LowestPrice
print DepTravelTime
print RetTravelTime
print ResultUrl
