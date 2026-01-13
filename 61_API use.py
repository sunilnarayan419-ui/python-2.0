# How to connect an API using Python 

import requests  

base_url = "https://pokeapi.co/api/v2/pokemon/pikachu"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url) 

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
        
    else: 
        print(f"Failed to retrieve data {response.status_code}")    
  
# ELEMENTS      
pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)   

# TESTING
if pokemon_info:
    print(f"{pokemon_info["name"].capitalize()}")
    print(f"{pokemon_info["id"]}")
    print(f"{pokemon_info["height"]}")
    print(f"{pokemon_info["weight"]}")  
    