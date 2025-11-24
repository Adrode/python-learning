import requests

def fetch_ip(url):
  try:
    response = requests.get(url, timeout=3)
    response.raise_for_status()
    return response.json()['origin']
  except requests.exceptions.Timeout:
    return "Timeout error"
  except requests.exceptions.ConnectionError:
    return "Connection error"
  except requests.exceptions.RequestException:
    return f"{response.status_code} Request error"

print(fetch_ip("https://httpbin.org/ip"))