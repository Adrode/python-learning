import requests

payload = {"pokemon": "pikachu", "power": 9000}

response = requests.post("https://httpbin.org/post", json=payload)

print(response.json()['json'])