import requests

response = requests.get('https://www.bc.edu/')

print(response.status_code)
print(response.text)


