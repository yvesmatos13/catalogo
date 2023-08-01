import json

import requests

with open("appsettings.json") as user_file:
  file_contents = user_file.read()

file = json.loads(file_contents) 

url = file["seriesAPI"]

response_API = requests.get(url)

series = json.loads(response_API.text)