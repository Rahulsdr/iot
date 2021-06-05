import requests
#from flask import Flask
API_KEY = "b105b8f9e575477e256ed67505ae6a44"
city = "kollam"
api_url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_KEY
response = requests.get(api_url).json()
print(response)
for k,v in response.items():
 print(k,v)

import pymysql
city=response['name']
lat=response['coord']['lat']
lon=response['coord']['lon']
temp=response['main']['temp']
feels_like=response['main']['feels_like']
pressure=response['main']['pressure']
humidity=response['main']['humidity']
sea_lvl=response['main']['sea_level']
ground_lvl=response['main']['grnd_level']
wind_spd=response['wind']['speed']

data={'City':city,'Latitude':lat,'Longitude':lon,'Temperature':temp,'WindSpeed':wind_spd,'FeelsLike':feels_like,'Pressure':pressure,'Humidity':humidity,'SeaLevel':sea_lvl,'GroundLevel':ground_lvl}
print(data)
conn=pymysql.connect(database='weather',user='Rahul',password='12345',host='localhost')
cur=conn.cursor()
cur.execute("INSERT INTO city_details(City,Latitude,Longitude,Temperature,WindSpeed,FeelsLike,Pressure,Humidity,SeaLevel,GroundLevel) VALUES (%(City)s,%(Latitude)s,%(Longitude)s,%(Temperature)s,%(WindSpeed)s,%(FeelsLike)s,%(Pressure)s,%(Humidity)s,%(SeaLevel)s,%(GroundLevel)s);",data)
conn.commit()
print('Saved to db')

