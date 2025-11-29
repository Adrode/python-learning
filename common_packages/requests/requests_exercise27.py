import requests

headers = {
  'X-API-Key': '12345abcde'
}
response = requests.get("https://httpbin.org/headers", headers=headers)
print(response.json())