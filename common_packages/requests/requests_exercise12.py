import requests

def fetch_url(url, timeout_sec):
  try:
    response = requests.get(url, timeout=timeout_sec)
  except requests.exceptions.Timeout:
    return "Timeout error"
  except requests.exceptions.RequestException:
    return f"{response.status_code} error"

  return response.json()

print(fetch_url("https://httpbin.org/delay/3", 1))
print(fetch_url("https://httpbin.org/delay/3", 5))