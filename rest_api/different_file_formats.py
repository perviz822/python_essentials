import json


url = 'rest_api/sample1.json'

with open (url,'r') as json_file:
 json_object = json.load(json_file)
 

print(json_object)
