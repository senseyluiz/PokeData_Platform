import requests
import json
from pathlib import Path

from scripts.utils.file_utils import save_to_json

BASE_URL = "https://pokeapi.co/api/v2/type/"

BASE_DIR = Path(__file__).resolve().parents[2]
OUTPUT_PATH = BASE_DIR / "data/lake/raw/types.json"

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


if __name__ == "__main__":
    types = extract_tipo()
    save_to_json(types, OUTPUT_PATH)
    print(f"{len(types)} tipos encontrados com sucesso")
