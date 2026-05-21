import pandas as pd
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
OUTPUT_PATH = BASE_DIR / "data/processed/pokemon.json"

pokemons_PATH = BASE_DIR / "data/lake/raw/pokemon.json"

df_pokemons = pd.read_json(pokemons_PATH)

dim_pokemon = [
    {
    "id_pokemon": pokemon["id"],
    "name": pokemon["name"],
    "nome_pokemon": pokemon["name"],
    "altura": pokemon["height"],
    "peso": pokemon["weight"],
    "url_imagem": pokemon["image"]
    }
    for id, pokemon in df_pokemons.iterrows()
]

def save_pokemon_to_json(data):
    print(f"Salvando em {OUTPUT_PATH}")
    with OUTPUT_PATH.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    save_pokemon_to_json(dim_pokemon)
