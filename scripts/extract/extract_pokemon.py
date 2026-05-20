import requests
import json
import os

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUTPUT_PATH = os.path.join(BASE_DIR, "data/lake/raw/pokemon.json")

def extract_pokemon():
    url = BASE_URL
    all_pokemons = []

    while url:
        print(f"Buscando dados da URL: {url}...")

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        for pokemon in data["results"]:
            pokemon_data = extract_pokemon_details(pokemon["url"])
            all_pokemons.append(pokemon_data)

        url = data["next"]

    return all_pokemons


def extract_pokemon_details(url):
    print(f"Detalhes: {url}")
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    return {
        "id": data["id"],
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "image": data["sprites"]["front_default"] or "",
        "types": [t["type"]["name"] for t in data["types"]],
        "abilities": [a["ability"]["name"] for a in data["abilities"]],
        "stats": {s["stat"]["name"]: s["base_stat"] for s in data["stats"]},
    }

def save_to_pokemons(data):
    print(f"Salvando em {OUTPUT_PATH}...")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    all_pokemons = extract_pokemon()
    save_to_pokemons(all_pokemons)
    print(f"{len(all_pokemons)} Pokémons encontrados com sucesso!")