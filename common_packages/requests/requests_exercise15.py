import requests

def fetch_random_user(url):
  try:
    response = requests.get(url, timeout=3)
    response.raise_for_status()
    result = response.json()['results']
    user_data = f"""First name: {result[0]['name']['first']}
Last name: {result[0]['name']['last']}
Email: {result[0]['email']}
Country: {result[0]['location']['country']}
Phone num.: {result[0]['phone']}"""
    return user_data
  except requests.exceptions.Timeout:
    return "Timeout error"
  except requests.exceptions.ConnectionError:
    return "Connection error"
  except requests.exceptions.RequestException:
    return f"{response.status_code} error"

print(fetch_random_user("https://randomuser.me/api/"))