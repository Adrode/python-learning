import requests

token = "moj_super_sekretny_token_12345"
headers = {'Authorization': f'Bearer {token}'}

response = requests.get("https://httpbin.org/bearer", headers=headers)
print(response.json())