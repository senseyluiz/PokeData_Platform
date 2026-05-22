import requests
import json
from pathlib import Path

from scripts.utils.file_utils import save_to_json

BASE_URL = "https://pokeapi.co/api/v2/ability/"

BASE_DIR = Path(__file__).resolve().parents[2]
OUTPUT_PATH = BASE_DIR / "data/lake/raw/abilities.json"

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




if __name__ == "__main__":
    abilities = extract_abilities()
    save_to_json(abilities, OUTPUT_PATH)
    print(f"{len(abilities)} habilidades encontrados com sucesso")
