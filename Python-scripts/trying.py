import urllib2
import json
from pprint import pprint
from operator import attrgetter

class City:
	def __init__(self, Name, Tags, Points):
		self.Name = Name
		self.Tags = Tags
		self.Points = Points


def rankCities(listOfCities, listofactivities, startdate, enddate):
	apikey = '&apikey=j3HAAFcwQG6n3X1Q0Ec84wgwZuDmwiFY'
	url = 'http://terminal2.expedia.com:80/x/activities/search?'
	for city in listOfCities:
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


url= 'http://terminal2.expedia.com/x/hotels?maxhotels=3&location=47.6063889,-122.3308333&radius=1km&apikey=j3HAAFcwQG6n3X1Q0Ec84wgwZuDmwiFY'
response = urllib2.urlopen(url).read()
data = json.loads(response)
mylist = data['HotelInfoList']
mylist = mylist['HotelInfo']
#mylist = mylist['Name']
for data in mylist:
	print(data['Name'])
#pprint(mylist)

berlin = City("Berlin", ['Adventure'],0)
montreal = City("Montreal",['Adventure'],0)
la = City("Los Angeles",['Adventure'],0)
activities = ['Adventures','Attractions','Show & Sport Tickets']
rankCities([berlin], activities, "2015-06-10", "2015-06-12")
print(berlin.Points)

# [filterCategories][nameofactivity][count]
# This function receives a list of cities
