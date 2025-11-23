import requests

headers = {'X-Client': 'Adrian-Tester'}
response = requests.get("https://httpbin.org/get", headers=headers)

print(response.json()["headers"])