import requests

parameters = {'page': 3, 'limit': 50}

response = requests.get("https://httpbin.org/get", params=parameters)

print(response.json()['args'])
# {'limit': '50', 'page': '3'}