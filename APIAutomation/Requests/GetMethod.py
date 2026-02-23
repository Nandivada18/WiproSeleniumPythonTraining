import requests
try:

    # make a get request to a api endpoint
    response = requests.get("https://videogamedb.uk:443/api/v2/videogame")
    print(response)

    #check if tym status code is 200 ok
    if response.status_code == 200:
        print("Status code is 200 k")
        #parse the json file
        data = response.json()
        print(data)
    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")