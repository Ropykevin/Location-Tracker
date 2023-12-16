import phonenumbers
from phonenumbers import geocoder
from my_phon import number
from phonenumbers import carrier
import opencage
import folium
from opencage.geocoder import OpenCageGeocode

pep_number=phonenumbers.parse(number)
location=geocoder.description_for_number(pep_number,"en")
print(location)


service_pro=phonenumbers.parse(number)
print(carrier.name_for_number(service_pro,"en"))

key = '6f1e72f41a164c6690886830857d6ca2'
geocoder=OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)
# print(results+254714670714)
lat=results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

my_map=folium.Map(location=(lat,lng),zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(my_map)
my_map.save("mylocation.html")


