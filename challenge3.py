import requests
import sys

def search_pokemon(name):
  #response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
  #pokemon_name = str(input("Your favorite pokemon: "))
  #response = requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(pokemon_name))
  response = requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(name))
  pokemon = response.json()
  print("Name: " + str.capitalize(pokemon["name"]))
  print("ID: " + str(pokemon["id"]))
  print("BaseXP: " + str(pokemon["base_experience"]))
  
if __name__ == "__main__":
  search_pokemon(sys.argv[1])

#Output1 Must store 6 pokemons and show information about them
#Name: <pokemon name>
#HP: <pokemon HP>
#Attacks: <pokemon attacks>
#Held Items: <pokemon items>

