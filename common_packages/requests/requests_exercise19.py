import requests

session = requests.Session()

session.headers.update({"X-Session": "test123"})
response = session.get("https://httpbingo.org/headers")

print(response.json())

session.close()