import requests
import json
import os

BASE_URL = "https://pokeapi.co/api/v2/ability/"
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUTPUT_PATH = os.path.join(BASE_DIR, "data/lake/raw/abilities.json")

def extract_abilities():
    url = BASE_URL
    all_abilities = []

    while url:
        print(f"Buscando dados de {url}...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        all_abilities.extend(data["results"])
        url = data["next"] # Busca pela próxima página

    return all_abilities

def save_abilities(data):
    print(f"Salvando em: {OUTPUT_PATH}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    abilities = extract_abilities()
    save_abilities(abilities)
    print(f"{len(abilities)} habilidades encontrados com sucesso")
