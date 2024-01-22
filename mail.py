import smtplib 
import imghdr 
from email.message import EmailMessage

a=input('enter time of 30 hourly observation:')
b=str(input('enter time of origin:'))
c=input('where the Meter go:')
d=str(input('wind speed v direction:'))
e=input('cloud_1 type:')
f=input('cloud_2 type:')
g=input('cloud_3 type/NSC:')
h=input('cloud_4 type/SKC:')
i=input('dry-bulb temp:')
j=input('wet-bulb temp:')
k=eval(input('C.L.P of digital bar:'))
l=eval(input('QNH of digital bar :'))
m=input('Dew point:')
n=input('relative humidity:')
o=input('present weather:').upper()
p=str(input('visibility/COVAK:'))
q=input('evaporation cups:')
r=input('Rainfall:')
k_r=round(k/70,2)
l_r=round(l/23,2)

import sys
from io import StringIO

sam=StringIO()
sys.stdout=sam

print(f"{a}z,{b}z,{c},{d}KT,{e},{f},{g},{h},{j},{i},{k},{k_r},{l},{l_r},{m},{n},{o},{p}Km,{q}")

magesa=sam.getvalue()
sys.stdout=sys.__stdout__

subs='sam'

#send_to=str(input('send to:'))
email='sam263708@gmail.com'
msg=EmailMessage()
msg['subject']=subs
msg['From']=email
msg['To']=email
msg.set_content(magesa)

#with open('deft.jpg','rb') as f:
  #file_data = f.read()
  #file_type = imghdr.what(f.name)
  #file_name = f.name

with smtplib.SMTP('localhost',1025) as sam:
  #sam.login(email,'ipsfwxsrkyhgstef') 
  sam.send_message(msg)
