import requests

while True:
    ui = input("Would you like to hear a dog fact? (y/n)")

    if ui == "y":
        url = 'https://dog-facts-api.herokuapp.com/api/v1/resources/dogs'
        param = {'number': 1}

        response = requests.get(url, params=param)

        if response.ok:
            print(response.json()[0]["fact"])
        else:
            print("There was an error connecting to the api. Please try again.")
            
    elif ui == 'n':
        break
    else:
        print(f"The command \"{ui}\" is not supported.")
