import requests

with requests.Session() as session:
  session.cookies.set('odwiedziny', '1')
  while True:
    response = session.get("https://httpbin.org/cookies")
    visited = int(response.json()['cookies']['odwiedziny'])
    if visited < 5:
      visited += 1
      response2 = session.get(f"https://httpbin.org/cookies/set?odwiedziny={visited}")
      print(response2.json())
    else:
      print(f"Site visited {visited} times")
      break

session.close()