import requests

session = requests.Session()
session.get("https://httpbin.org/cookies/set?uzytkownik=Jan")
response1 = session.get("https://httpbin.org/cookies")
print(response1.json())
session.close()

requests.get("https://httpbin.org/cookies/set?uzytkownik=Jan")
response2 = requests.get("https://httpbin.org/cookies")
print(response2.json())