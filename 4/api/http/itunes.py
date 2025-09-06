import requests
import sys
import json

if len(sys.argv) < 2:
    sys.exit("Expected Track Name")

res = requests.get( 
    "https://itunes.apple.com/search?entity=song&limit=30&term=" + sys.argv[1]
)
data = res.json()
for result in data["results"]:
    print(result["trackName"])
