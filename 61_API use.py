# How to connect an API using Python (PokéAPI)

import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon"


def get_pokemon_info(name):
    url = f"{BASE_URL}/{name.lower()}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ Failed to retrieve data (Status Code: {response.status_code})")
            return None

    except requests.exceptions.RequestException as e:
        print(f"⚠ Network error: {e}")
        return None


# -------------------------
# USER INPUT
# -------------------------
pokemon_name = input("Enter Pokémon name: ")

pokemon_info = get_pokemon_info(pokemon_name)

# -------------------------
# OUTPUT
# -------------------------
if pokemon_info:
    print("\n🧾 Pokémon Details")
    print("-" * 20)
    print(f"Name   : {pokemon_info['name'].capitalize()}")
    print(f"ID     : {pokemon_info['id']}")
    print(f"Height : {pokemon_info['height']}")
    print(f"Weight : {pokemon_info['weight']}")

    print("\nAbilities:")
    for ability in pokemon_info["abilities"]:
        print(f"- {ability['ability']['name'].capitalize()}")

    