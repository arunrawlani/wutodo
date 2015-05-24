import cgi
import json
import urllib2
from random import randint 

class Result :
    def __init__(self,Name,Price,OutgoingDate,ReturningDate,url,img):
        self.Name = Name
        self.Price = Price
        self.OutgoingDate = OutgoingDate
        self.ReturningDate = ReturningDate
        self.url = url
        self.img = img

imgdict={
            "Berlin":"http://s14.postimg.org/sq8icx7pd/Berlin_3.jpg",
            "London":"http://cdn.londonandpartners.com/visit/london-organisations/houses-of-parliament/63950-640x360-london-icons2-640.jpg",
            "Montreal":"http://s3.postimg.org/kaepl85wz/Montreal_1.jpg",
            "Dubai":"http://www.netflights.com/media/189043/dubai_02_681x298.jpg",
            "Phuket":"http://s1.postimg.org/ydfi05q27/Phuket_2.jpg",
            "Bali":"http://s14.postimg.org/3mmuf6kox/Bali_1.jpg",
            "Paris":"http://upload.wikimedia.org/wikipedia/commons/e/e6/Paris_Night.jpg"
        }        
Destination = ["Berlin","London","Montreal","Dubai","Phuket","Paris","Bali"]

form = cgi.FieldStorage()
BegDate = "2015-06-10"
EndDate = "2015-06-12"

if "firstname" in form:
    DepCity = form["firstname"].value
if not "firstname" in form :
    DepCity = "Jakarta"
ArrCity = DepCity
while ArrCity == DepCity :
    ArrIndex = randint(0,6)
    ArrCity = Destination[ArrIndex]

if "departure" in form:
    BegDate = form["departure"].value
    if "return" in form:
        EndDate = form["return"].value

ArrImg = imgdict.get(ArrCity)

DepCity.replace(" ", "%20")
ArrCity =ArrCity.replace(" ", "%20")

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
Price = str(data["PackageSearchResultList"]["PackageSearchResult"]["PackagePrice"]["TotalPrice"]["Value"])+" "+data["PackageSearchResultList"]["PackageSearchResult"]["PackagePrice"]["TotalPrice"]["Currency"]
ResultUrl = data["PackageSearchResultList"]["PackageSearchResult"]["DetailsUrl"]


print '''Content-type: text/html \n\n
<html>
<head><title>Your trips</title></head>
	<link href='http://fonts.googleapis.com/css?family=Nunito:400,300' rel='stylesheet' type='text/css'>
	<body style="font-family:'Nunito',sans-serif;background-color:white;color:black;">
		
		<div style="width:600px;background-color:#F2F2F2;margin-left:auto;margin-right:auto;min-height:650px;border-radius:15px">
			<div style="text-align:center;"><h1>Where will you go?</h1></div>
    <div style="background-image:url(%s);width:600px;min-height:200px;background-size:contain;
					background-repeat:no-repeat;vertical-align:middle;text-align:center">
			</div><br>
			<div style:"text-align:center;margin-top:15px;margin-bottom:15px"><a href=%s>%s</a>  %s<div><br>
			
   </div>
	</body>
</html>''' %(ArrImg,PackageUrl,ArrCity,Price)
