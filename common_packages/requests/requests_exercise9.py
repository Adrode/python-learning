import requests

def send_json(url, data):
  response = requests.post(f"{url}/post", json=data)

  if response.status_code != 200:
    return f"Error - code: {response.status_code}"
  else:
    return response.json()
  
print(send_json("https://httpbin.org", {'pokemon': 'pikachu', 'weight': 60}))