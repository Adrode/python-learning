import requests

def get_pokemon_info():
  while True:
    pokemon_name = input("Type pokemon name: ")
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    if response.status_code != 200:
      print("This pokemon does not exist. Type again.")
      continue
    else:
      pokemon_data = response.json()
      print(f"Name: {pokemon_data['name']}")
      print(f"Base XP: {pokemon_data['base_experience']}")
      print(f"Height: {pokemon_data['height']}")
      print(f"Weight: {pokemon_data['weight']}")
      pokemon_types = [item['type']['name'] for item in pokemon_data['types']]
      print(f"Types: {", ".join(pokemon_types)}")
      print("Stats:")
      for item in pokemon_data['stats']:
        print(f" {item['stat']['name'].capitalize()}: {item['base_stat']}")
      break

get_pokemon_info()