import requests

session = requests.Session()
session.headers.update({
  "User-Agent": "MojBot/1.0",
  "Accept-Language": "pl-PL"
})
response1 = session.get("https://httpbin.org/headers")
print(response1.json())
response2 = session.get("https://httpbin.org/headers")
print(response2.json())
response3 = session.get("https://httpbin.org/headers")
print(response3.json())

session.close()