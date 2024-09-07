import requests
import json
import pyttsx3
city=input("City: ")
url=f"https://api.weatherapi.com/v1/current.json?key=e14aa328cdf94a5dbf860646241507&q={city}"
r=requests.get(url)
# print(r.text)
dic=json.loads(r.text)
x=dic["current"]["temp_c"]

l=[ f"Region : {dic["location"]["region"]}",
   f"Country : {dic["location"]["country"]}",
    f"Temperature : {dic["current"]["temp_c"]} degrees",
    f"Condition : {dic["current"]["condition"]["text"]}",
   ]

string=f"The current weather in {city} is : "
engine = pyttsx3.init()
engine.say(string)
engine.runAndWait()
print(string)

for x in l:
    engine = pyttsx3.init()
    st=f"{x}"
    engine.say(st)
    engine.runAndWait()
    print(x)