import json

#data to save
data = {
    "name": "Karma",
    "age": 22,
    "skills": ["python", "Git", "File Handling"]
}

#write to json file
with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent = 4)
    
print("JSON file written successfully!")



