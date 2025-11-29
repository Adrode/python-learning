import requests

response = requests.get("https://httpbin.org/image/jpeg") 
with open("download.jpg", 'wb') as file:
  file.write(response.content)