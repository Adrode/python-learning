import requests

with requests.Session() as session:
  response1 = session.get("https://httpbin.org/cookies/set/atest/1")
  print(f"1: {session.cookies.get_dict()}")

  response1 = session.get("https://httpbin.org/cookies/set/btest/2")
  print(f"2: {session.cookies.get_dict()}")

  response1 = session.get("https://httpbin.org/cookies/set/ctest/3")
  print(f"3: {session.cookies.get_dict()}")

session.close()