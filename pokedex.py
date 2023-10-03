import requests
import sys

def search_pokemon(name):
  #response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
  pokemon_name = str(input("Your favorite pokemon: "))
  response = requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(pokemon_name))
  pokemon = response.json()
  print("Name: " + str.capitalize(pokemon["name"]))
  print("ID: " + str(pokemon["id"]))
  #print("BaseXP: " + str(pokemon["levels"][0][1]))
  
if __name__ == "__main__":
  search_pokemon(sys.argv[1])
  
#Output1
#Name: <pokemon name>
#ID: <pokemon ID>
#Base XP: <pokemon baseXP>

#Output1
#Name: <pokemon name>
#HP: <pokemon HP>
#Attacks: <pokemon attacks>
#Held Items: <pokemon items>

