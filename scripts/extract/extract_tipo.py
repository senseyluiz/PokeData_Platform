import requests
import json
import os

BASE_URL = "https://pokeapi.co/api/v2/type/"
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUTPUT_PATH = os.path.join(BASE_DIR, "data/lake/raw/types.json")

def extract_tipo():
    url = BASE_URL
    all_types = []

    while url:
        print(f"Buscando dados de {url}")
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        all_types.extend(data["results"])
        url = data["next"] # Busca pela próxima página

    return all_types

def save_to_json(data):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    types = extract_tipo()
    save_to_json(types)
    print(f"{len(types)} tipos encontrados com sucesso")
