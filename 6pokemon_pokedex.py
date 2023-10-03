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
        print("HP: " + str(pokemon["stats"][0]["base_stat"]))
        num_attacks = len(pokemon["moves"])
        print("Attacks: " + str(num_attacks))
        held_items = [item["item"]["name"] for item in pokemon["held_items"]]
        if held_items:
            print("Held Items: " + ", ".join(held_items))
        else:
            print("Held Items: None")

if __name__ == "__main__":
    print("Enter your six Pokemon names below:")
    search_pokemon()