import pandas as pd
import json
from pathlib import Path

from scripts.utils.file_utils import save_to_json

BASE_DIR = Path(__file__).resolve().parents[2]
OUTPUT_PATH = BASE_DIR / "data/processed/"

dim_pokemon_OUTPUT_PATH = OUTPUT_PATH / "dim_pokemon.json"

pokemons_PATH = BASE_DIR / "data/lake/raw/pokemon.json"

df_pokemons = pd.read_json(pokemons_PATH)

dim_pokemon = [
    {
    "id_pokemon": pokemon["id"],
    "nome_pokemon": pokemon["name"],
    "altura": pokemon["height"],
    "peso": pokemon["weight"],
    "url_imagem": pokemon["image"]
    }
    for _, pokemon in df_pokemons.iterrows()
]


if __name__ == "__main__":
    save_to_json(dim_pokemon, dim_pokemon_OUTPUT_PATH)
