import requests

payload = {'username': 'Adrian', 'password': 'test'}
req = requests.post("https://httpbin.org/post", data=payload)
req_dict = req.json()

print(req_dict)
# returns
# {'args': {}, 'data': '', 'files': {}, 'form': {'password': 'test', 'username': 'Adrian'},
#  'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Content-Length': '29',
#              'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'httpbin.org',
#              'User-Agent': 'python-requests/2.31.0', 'X-Amzn-Trace-Id': 'Root=1-69208f55-278e6bd37c4534d7006c2bc8'},
#   'json': None, 'origin': '83.4.167.93', 'url': 'https://httpbin.org/post'}

print(req_dict['form'])
# returns
# {'password': 'test', 'username': 'Adrian'}