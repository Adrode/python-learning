import requests

files = {'file': open('test2.txt', 'rb')}
data = {'author': 'Adrian', 'description': 'Duckin Duck'}
response = requests.post("https://httpbin.org/post", files=files, data=data)
print(response.json())