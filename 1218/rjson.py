import json

with open("data.json", "r") as json_file:
    data = json.load(json_file)
    
print ("Data from JSON file:", data)