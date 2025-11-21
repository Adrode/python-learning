import requests

pokemon_name = input("Type pokemon name: ")

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")

if response.status_code != 200:
  print(f"{response.status_code} Pokemon not found")
else:
  pokemon_data = response.json()
  print(f"Name: {pokemon_data['name']}")
  print(f"Base XP: {pokemon_data['base_experience']}")
  print(f"Types: {[item['type']['name'] for item in pokemon_data['types']]}")