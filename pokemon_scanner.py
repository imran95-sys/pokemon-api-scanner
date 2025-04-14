import sys
import requests
import json

def get_pokemon_data(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return {"error": "Pokémon not found."}

    data = response.json()
    return {
        "name": data["name"],
        "base_experience": data["base_experience"],
        "height": data["height"],
        "weight": data["weight"],
        "abilities": [a["ability"]["name"] for a in data["abilities"]]
    }

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Please provide a Pokémon name."}))
    else:
        result = get_pokemon_data(sys.argv[1])
        print(json.dumps(result, indent=4))

