import requests

def search_pokemon():
    pokemon_list = []
    while len(pokemon_list) < 6:
        pokemon_name = input(f"Enter Pokémon {len(pokemon_list) + 1}: ").lower()
        pokemon_list.append(pokemon_name)
    
    for pokemon_name in pokemon_list:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
        pokemon = response.json()
        print("Name: " + str.capitalize(pokemon["name"]))
        print("ID: " + str(pokemon["id"]))
        print("BaseXP: " + str(pokemon["base_experience"]))

if __name__ == "__main__":
    print("Enter your six Pokemon names below:")
    search_pokemon()
