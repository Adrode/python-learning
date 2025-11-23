import requests

def safe_url(url):
  try:
    response = requests.get(url, timeout=3)
  except requests.exceptions.ConnectionError:
    return "Connection error"
  except requests.exceptions.Timeout:
    return "Timeout error"
  except requests.exceptions.RequestException:
    return f"{response.status_code} error"
  if response.status_code == 404:
    return f"{response.status_code} not found"
  if response.status_code == 500:
    return f"{response.status_code} server error"
  
  return response.json()

print(safe_url("https://httpbin.org/status/404"))
print(safe_url("https://httpbin.org/status/500"))
print(safe_url("https://thisdomaindoesnotexist123123.com"))