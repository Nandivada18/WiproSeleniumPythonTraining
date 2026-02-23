import json

#read the json file load method
with open("C://Users//prasa//PycharmProjects//PythonAdvancePrograming//Dataformats//employee.json", 'r') as file:
    data = json.load(file)

print(data)
print(data["name"])

with open("C://Users//prasa//PycharmProjects//PythonAdvancePrograming//Dataformats//nestedjson.json", 'r') as file:
    data = json.load(file)

email = data["user"]["profile"]["email"]
print(email)

#writing to json file - dump method()
data = {
  "name": "Harsha",
  "role": "Tester",
  "experience": 5,
  "skills": ["Python", "Automation", "API"]
}
with open("C://Users//prasa//PycharmProjects//PythonAdvancePrograming//Dataformats//writejson.json", 'w') as file:
    json.dump(data,file)

#update or modify the json file
#modify data
#write it back to the file

with open("C://Users//prasa//PycharmProjects//PythonAdvancePrograming//Dataformats//updatejson.json", 'r') as file:
    data = json.load(file)
#update the value
data["experience"] = 6

#write back
with open("C://Users//prasa//PycharmProjects//PythonAdvancePrograming//Dataformats//updatejson.json", 'w') as file:
    json.dump(data, file, indent = 4)