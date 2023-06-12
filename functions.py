import requests
import json

key = 'cVx8cdLFLJree03QdRHdhr4tfndlWfgA60SRDrTR'

def apiRequest(key, date):
    data = requests.get(f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={date}&camera=fhaz&api_key={key}')
    serialized_data = json.dumps(data.json(), indent=3)
    with open(f'cache/{date}.json', 'w') as output:
        output.write(serialized_data)
