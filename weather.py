#import json
import requests
City = input('Hello\nPlease enter city')
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+City+'&APPID=4c151bd4d9683df3c1565451375278e3')
response = r.json()
Temp = ((response['main'])['temp']) - 273
print('The tempreture in',City, 'now is', Temp , 'Deg Celcious')
