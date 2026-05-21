import pandas as pd
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
OUTPUT_PATH = BASE_DIR / "data/processed/"

dim_pokemon_OUTPUT_PATH = OUTPUT_PATH / "dim_pokemon.json"

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
    for _, pokemon in df_pokemons.iterrows()
]

def save_to_json(data, output):
    print(f"Salvando em {output}")
    with output.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


OUTPUT_PATH.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    save_to_json(dim_pokemon, dim_pokemon_OUTPUT_PATH)
