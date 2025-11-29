import requests

response = requests.get("https://httpbin.org/basic-auth/user/passwd", auth=('user', 'passwd'))
print(response.json())
# poprawna autoryzacja

response2 = requests.get("https://httpbin.org/basic-auth/user/passwd")
print(response2.json())
# błąd w autoryzacji, brak auth