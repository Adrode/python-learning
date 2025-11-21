import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=50")

if response.status_code != 200:
  print(f"No response. Code: {response.status_code}")
else:
  pokemon_data = response.json()
  pokemon_list = [item['name'] for item in pokemon_data['results']]
  for i, item in enumerate(pokemon_list):
    print(f"{i+1}. {item}")