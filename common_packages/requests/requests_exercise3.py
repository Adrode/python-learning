import requests

pokemon_name = input("Type pokemon name: ")
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")

def get_pokemon_moves(r, name):
  if r.status_code != 200:
    print(f"No response. Code: {r.status_code}")
  else:
    pokemon_data = r.json()
    pokemon_moves = [item['move']['name'] for item in pokemon_data['moves']]
    pokemon_moves.sort()
    print(f"{name} has {len(pokemon_moves)} moves:")
    for item in pokemon_moves:
      print(f"- {item}")
  
get_pokemon_moves(response, pokemon_name)