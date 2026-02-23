import requests
from requests.auth import HTTPBasicAuth
#1.Name and Email only
try:
    # make a get request to a api endpoint
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    print(response)
    #check if tym status code is 200 ok
    if response.status_code == 200:
        print("Status code is 200 k")
        #parse the json file
        Users = response.json()
        #Name
        for i in Users:
            print(i["name"])
        #email
            print(i["email"])
    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

#2. with parameters print no.of posts returned
response = requests.get("https://jsonplaceholder.typicode.com/users", params={"userId":1})
print(response)
    #check if tym status code is 200 ok
if response.status_code == 200:
    print("Status code is 200 k")
    #parse the json file
    Users = response.json()
    print(len(Users))
else:
    print(f"Error: Received status code {response.status_code}")

#3.Post request and verify status code 201
data = {
    "name": "Prasad",
    "userId": 209,
    "car": "swag"
}
response = requests.post("https://jsonplaceholder.typicode.com/users",json=data)
print(response)
    #check if tym status code is 200 ok
if response.status_code == 201:
    print("Status code is 201 k")
    #parse the json file
    Users = response.json()
else:
    print(f"Error: Received status code {response.status_code}")

#4.Differece between data and json = in requests.post()
'''
Data:
* it sends data as form data
* used for form submission
* content-type is application/form

Json:
* it sends data as json format
* it coverts python to json
* content-type is application/json
'''
 #5. check response status is not 200
response = requests.post("https://jsonplaceholder.typicode.com/users")
print(response)
    #check if tym status code is 200 ok
#if response.status_code != 200:
    #raise Exception(f"Error: Received status code {response.status_code}")

#6.usernames in uppercase
response = requests.get("https://jsonplaceholder.typicode.com/users")
print(response)
#check if tym status code is 200 ok
if response.status_code == 200:
    print("Status code is 200 k")
    #parse the json file
    Users = response.json()
    for i in Users:
        print(i["username"].upper())

#7.Timeout handling exception 2 sec
try:
    # make a get request to a api endpoint
    response = requests.get("https://jsonplaceholder.typicode.com/users",timeout=2)
    print(response)
    #check if tym status code is 200 ok
    if response.status_code == 200:
        print("Status code is 200 k")
except requests.exceptions.Timeout:
    print("Time out")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

#10.Fetch posts and save response json
import json
response = requests.get("https://jsonplaceholder.typicode.com/users",timeout=2)
print(response)
#check if tym status code is 200 ok
if response.status_code == 200:
    print("Status code is 200 k")
    Users = response.json()
    with open("C://Users//prasa//PycharmProjects//PythonAdvancePrograming//PythonAdvancePrograming//PythonAdvancePrograming//Dataformats//posts.json","w") as file:
        json.dump(Users,file,indent=4)
    print("compledted")