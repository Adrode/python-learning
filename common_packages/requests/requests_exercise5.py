import requests

payload = {'name': 'Adrian', 'age': 25}

response = requests.post(f"https://httpbin.org/post", data=payload)

print(response.text)
# "json": null
# "User-Agent": "python-requests/2.31.0"