import requests

def fetch_file(url):
  try:
    headers = {
      "User-Agent": "Mozilla/5.0 (compatible; MyPythonScript/1.0)"
    }
    response = requests.get(url, timeout=3, headers=headers)
    response.raise_for_status()
    extension = response.headers['content-type'].split('/')[1]
    
    with open(f"downloaded.{extension}", 'wb') as f:
      f.write(response.content)

    return "OK"
  except requests.exceptions.Timeout:
    return "Timeout"
  except requests.exceptions.ConnectionError:
    return "Connection error"
  except requests.exceptions.RequestException as e:
    return e
  
print(fetch_file("https://i.imgur.com/8Km9tLL.png"))