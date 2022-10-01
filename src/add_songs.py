import requests
import constants
import json
import re

# file-specific constants 
playlist_id = "23qmu30swQpcyappYycdgB" # this should be configurable
get_endpoint_url = "https://api.spotify.com/v1/recommendations?"

# FILTERS
limit = 6
market = "US"
seed_genres="hip-hop"
target_danceability=0.6
seed_artists="699OTQXzgjhIYAHMy9RyPD"

# uris
uris = []

# query for the songs based on the inputted filters
query = f'{get_endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}&target_danceability={target_danceability}'

# get the songs based on the query params
response = requests.get(query, headers={"Content-Type":"application/json", 
"Authorization":"Bearer " + constants.TOKEN})

# get the json response
json_response = response.json()

# put all the uris in a list
for i in json_response['tracks']:
            uris.append(i)

# make the uris into a string
uriStrings = json.dumps(uris)
# find all instances of track id's in the uris using regex
request = re.finditer("spotify:track:\w{22}", uriStrings)

# add all the track id's to one string to be passed as the data in the post request
request_data = '{"uris": ['
for i in request:
    request_data += '"' + i.group() + '",'

# remove the last comma
request_data = request_data.removesuffix(",")
# close the brackets for the data
request_data += ']}'

# playlist endpoint
playlist_endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

# post request
response = requests.post(url = playlist_endpoint_url, 
                        data = request_data,
                        headers={"Content-Type":"application/json", 
                       "Authorization":"Bearer " + constants.TOKEN})

# print the response in case an error occurs
print(response)