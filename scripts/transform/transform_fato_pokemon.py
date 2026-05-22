import pandas as pd
from pathlib import Path
import json

from scripts.utils.file_utils import save_to_json

BASE_DIR = Path(__file__).resolve().parents[2]
OUTPUT_PATH = BASE_DIR / "data/processed"

fato_pokemon_OUTPUT_PATH = OUTPUT_PATH / "fato_pokemon_stats.json"

pokemons_PATH = BASE_DIR / "data/lake/raw/pokemon.json"

df_pokemons = pd.read_json(pokemons_PATH)

fato_pokemon_stats = [
    {
        "id_pokemon": pokemon["id"],
        "hp": pokemon["stats"].get("hp"),
        "attack": pokemon["stats"].get("attack"),
        "defense": pokemon["stats"].get("defense"),
        "special_attack": pokemon["stats"].get("special-attack"),
        "special_defense": pokemon["stats"].get("special-defense"),
        "speed": pokemon["stats"].get("speed")
    }
    for _, pokemon in df_pokemons.iterrows()
]


if __name__ == "__main__":
    save_to_json(fato_pokemon_stats, fato_pokemon_OUTPUT_PATH)