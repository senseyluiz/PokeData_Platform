import requests
import json
from pathlib import Path

from scripts.utils.file_utils import save_to_json

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
BASE_DIR = Path(__file__).resolve().parents[2]
OUTPUT_PATH = BASE_DIR / "data/lake/raw/pokemon.json"

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


if __name__ == "__main__":
    all_pokemons = extract_pokemon()
    save_to_json(all_pokemons, OUTPUT_PATH)
    print(f"{len(all_pokemons)} Pokémons encontrados com sucesso!")