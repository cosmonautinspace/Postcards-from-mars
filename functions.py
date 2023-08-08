import requests
import json

key = ''

def apiRequest(key, date, rover):
    data = requests.get(f'https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos?earth_date={date}&camera=FHAZ&api_key={key}')
    serialized_data = json.dumps(data.json(), indent=3)
    with open(f'cache/{rover}/{date}.json', 'w') as output:
        output.write(serialized_data)
