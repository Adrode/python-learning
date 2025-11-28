import requests

session = requests.Session()

session.cookies.set('user', 'jan_kowalski')

response1 = session.get("https://httpbin.org/cookies")
print(response1.json())

response2 = session.get("https://httpbin.org/headers")
print(response2.json())

session.cookies.clear()
response3 = session.get("https://httpbin.org/headers")
print(response3.json())

session.close()