import requests

headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10)"}
response = requests.get("https://httpbin.org/get", headers=headers, timeout=3)

print(response.text)