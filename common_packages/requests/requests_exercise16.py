import requests

def safe_url(url):
  try:
    response = requests.get(url, timeout=3)
    response.raise_for_status()
    return response.json()
  except requests.exceptions.Timeout:
    return "Timeout"
  except requests.exceptions.ConnectionError:
    return "Connection error"
  except requests.exceptions.RequestException:
    return None

print(safe_url("https://randomuser.me/api/"))
print(safe_url("http://nieistnieje123.pl"))