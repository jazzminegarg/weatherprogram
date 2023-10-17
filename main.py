import requests
import json
import os
city=input("enter the name of the city")
url=f"https://api.weatherapi.com/v1/current.json?key=01e168a1d6744ee3b1b154240231104&q={city}"
r=requests.get(url)
print(r.text)
wdic=json.loads(r.text)
w=wdic["current"]["temp_c"]
print("the current weather in ",city ,"is ",w," degrees")