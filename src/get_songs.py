import requests
import constants

get_endpoint_url = "https://api.spotify.com/v1/recommendations?"

# FILTERS
limit = 5
market = "US"
seed_genres="hip-hop"
target_danceability=0.9
seed_artists="699OTQXzgjhIYAHMy9RyPD"

# uris
uris = []

query = f'{get_endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}&target_danceability={target_danceability}'

response = requests.get(query, headers={"Content-Type":"application/json", 
"Authorization":"Bearer " + constants.TOKEN})

json_response = response.json()

for i in json_response['tracks']:
            uris.append(i)
            print(f"\"{i['name']}\" by {i['artists'][0]['name']}")