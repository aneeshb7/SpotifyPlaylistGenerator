import json
import requests
import constants

# constants
endpoint_url = f"https://api.spotify.com/v1/users/{constants.USER_ID}/playlists"

request_body = json.dumps({
          "name": "Playlist for Monica", # this should be configurable
          "description": "For the gf", # this should be configurable
          "public": False # keep it private for now
        })

response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                        "Authorization":"Bearer " + constants.TOKEN})

print(response.status_code)