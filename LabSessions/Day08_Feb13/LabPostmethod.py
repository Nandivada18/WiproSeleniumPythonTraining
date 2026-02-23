import requests

#Post
try:

    # make a post request to a api endpoint
    response = requests.post("https://fakestoreapi.com/products")
    print(response)

    #check if tym status code is 200 ok
    if response.status_code == 201:
        print("Status code is 201 k")
        #parse the json file
        data = response.json()
        print(data)
    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")