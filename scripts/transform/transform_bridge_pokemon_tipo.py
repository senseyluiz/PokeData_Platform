import pandas as pd
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parents[2]
OUTPUT_PATH = BASE_DIR / "data/processed"

bridge_pokemon_tipo_PATH = OUTPUT_PATH / "bridge_pokemon_tipo.json"

pokemons_PATH = BASE_DIR / "data/lake/raw/pokemon.json"
tipo_PATH = BASE_DIR / "data/processed/dim_tipo.json"

df_pokemons = pd.read_json(pokemons_PATH)

with open(tipo_PATH) as json_file:
    dim_tipo = json.load(json_file)

tipo_map = {tipo["nome_tipo"]: tipo["id_tipo"] for tipo in dim_tipo}

bridge_pokemon_tipo = []

for _, pokemon in df_pokemons.iterrows():
    id_pokemon = pokemon["id"]

    for tipo in pokemon["types"]:
        bridge_pokemon_tipo.append(
            {
                "id_pokemon": id_pokemon,
                "id_tipo": tipo_map[tipo],
            }
        )

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

def save_to_json(data, output):
    with open(output, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    save_to_json(bridge_pokemon_tipo, bridge_pokemon_tipo_PATH)