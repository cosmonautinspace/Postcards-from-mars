import requests
import json 

x = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key=DEMO_KEY")
print(x.json())
data = json.dumps(x.json())

with open("sample.json", "w") as outfile:
    outfile.write(data)