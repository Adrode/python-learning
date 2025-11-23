import requests

search = input("Search: ")
max_results = input("Max results: ")

parameters = {'search': search, 'max_results': max_results}

response = requests.get("https://httpbin.org/get", params=parameters)

print(response.url)
# https://httpbin.org/get?search=kekw&max_results=50