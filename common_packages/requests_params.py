import requests

payload = {'page': 2, 'count': 25}
response = requests.get("https://httpbin.org/get", params=payload)

print(response.url) # returns "https://httpbin.org/get?page=2&count=25"
