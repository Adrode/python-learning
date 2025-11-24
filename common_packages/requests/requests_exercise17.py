import requests

def fetch_img(url):
  try:
    headers = {
      "User-Agent": "Mozilla/5.0 (compatible; MyPythonScript/1.0)"
    }
    response = requests.get(url, timeout=3, headers=headers)
    response.raise_for_status()
    with open("output.png", 'wb') as f:
      f.write(response.content)
    
    return "OK"
  except requests.exceptions.Timeout:
    return "Timeout"
  except requests.exceptions.ConnectionError:
    return "Connection error"
  except requests.exceptions.RequestException as e:
    return e

print(fetch_img("https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png"))