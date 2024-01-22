from flask import Flask,render_template,url_for
from flask import Request
import json
import requests
from requests.auth import HTTPBasicAuth
from datetime import *



app = Flask(__name__)

C_key='3IBPTrAJC26lgv4PD0TflGsfUUNr4TG0'
C_secret='7IMLyoAAw9CGAGaM'
auth_url='https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

def sam(): 
  data=(requests.get(auth_url,auth=HTTPBasicAuth(C_key,C_secret))).json()
  return data['access_token']
  
base_url='http://41.59.184.85:801/'
endpoint='https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl'
endpoint_s='https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate'
headers={"Authorization":"Bearer %s"%sam()}

body={
    "ShortCode":"600364",
    "ResponseType":"Completed",
    "ConfirmationURL":base_url+"/c2b/confirm",
    "ValidationURL":base_url+"/c2b/validate"}

r_body={
    "ShortCode":"600364",
    "CommandID":"CustomerPayBillOnline",
    "Amount":"100",
    "Msisdn":"255763480309",
    "BillRefNumber":"test123"
}

@app.route('/token')
def home():
  data = sam()
  return render_template('test.html',data=data)
  
app.route('/c2b/confirm',methods=['POST'])
def confirm():
  data=request.get_json()
  file= open('test.json','a')
  file.write(json.dumps(data))
  file.close()
  return {"ResultCode":0,"ResultDesc":"Accepted"}

app.route('/c2b/validate',methods=['POST'])
def validate():
  data=request.get_json()
  file= open('test_a.json','a')
  file.write(json.dumps(data))
  file.close()
  return {"ResultCode":0,"ResultDesc":"Accepted"}

@app.route('/register')
def register():
  response_data=requests.post(endpoint,
  json=body,
  headers=headers)
  #data=(json.dumps(response_data)).json()
  return response_data.json()

@app.route('/simulate')
def simulate():
  response_data=requests.post(endpoint_s,
  json=r_body,
  headers=headers)
  return response_data.json()
  
def location_time(utc_with_tz):
  localtime=datetime.utcfromtimestamp(utc_with_tz)
  return localtime.time() 


@app.route('/weather')
def weather():
	city_name='Dar-es-salaam'
	apk_key='36c2eb356b5529000c2a763deba7b1d9'
	
	url_weather="http://api.openweathermap.org/data/2.5/weather?q="+city_name + "&appid="+apk_key
	
	response=requests.get(url_weather)
	weather_info=response.json()	
	
	#tfield.delete("1.0","end")
	
	if weather_info['cod']==200:
		kelvin=273.15
		
	
		temp=float(weather_info['main']['temp']-kelvin)
		feels_like=float(weather_info['main']['feels_like']-kelvin)
		Prss=weather_info['main']['pressure']
		Hum=weather_info['main']['humidity']
		W_s=weather_info['wind']['speed']*3.6
		S_rise=weather_info['sys']['sunrise']
		S_set=weather_info['sys']['sunset']
		Tzone=weather_info['timezone']
		Cloudy=weather_info['clouds']['all']
		name=weather_info['name']
		descpt=weather_info['weather'][0]['description']
		
		S_time=location_time(S_rise+Tzone)
		S_set=location_time(S_set+Tzone)
		
		weather=f'''
		Weather of:{city_name} Region
		Temperature:{temp}°\C
		feels_like in:{feels_like}°\C
		Pressure:{Prss} hpa
		Humidity:{Hum}%
		sunrise at {S_time}
		sunset at  {S_set}
		Cloud : {Cloudy}%
		Info :{descpt}'''
	else:
		weather=f'\n\tWeather for "{city_name}"  not found!  \n\tKindly Enter Valid City Name '
	return weather


 
if __name__=='__main__':
  app.run(host='0.0.0.0',port=4000,debug=True)