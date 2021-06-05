import requests

#from flask import Flask

API_KEY = "b105b8f9e575477e256ed67505ae6a44"

city = "kollam"

api_url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_KEY

response = requests.get(api_url).json()

print(response)

for k,v in response.items():

 print(k,v)
