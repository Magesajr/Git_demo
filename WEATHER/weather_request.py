import requests 
import json


def weather():
	city_name='Dar-es-salaam'
	apk_key='36c2eb356b5529000c2a763deba7b1d9'
	
	url_wearther="http://api.openweathermap.org/data/2.5/weather?q="+city_name + "&appid="+apk_key
	
	response=requests.get(url_wearther)
	weather_info=response.json()
	
	if weather_info['cod']==200:
		Kelvin= 273
		
	return  weather_info
	
print('sam\'s father')	 

print(weather())