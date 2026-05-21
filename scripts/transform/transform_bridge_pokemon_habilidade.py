import pandas as pd
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parents[2]
OUTPUT_PATH = BASE_DIR / "data/processed"

bridge_pokemon_habilidade_PATH = OUTPUT_PATH / "bridge_pokemon_habilidade.json"

pokemons_PATH = BASE_DIR / "data/lake/raw/pokemon.json"
habilidade_PATH = OUTPUT_PATH / "dim_habilidade.json"

df_pokemons = pd.read_json(pokemons_PATH)

with open(habilidade_PATH, encoding="utf-8") as json_file:
    dim_habilidade = json.load(json_file)

habilidade_map = {habilidade["nome_habilidade"] : habilidade["id_habilidade"] for habilidade in dim_habilidade}

bridge_pokemon_habilidade = []

for _, pokemon in df_pokemons.iterrows():
    id_pokemon = pokemon["id"]

    for habilidade in pokemon["abilities"]:
        bridge_pokemon_habilidade.append(
            {
                "id_pokemon": id_pokemon,
                "id_habilidade": habilidade_map[habilidade]
            }
        )


OUTPUT_PATH.mkdir(parents=True, exist_ok=True)


def save_to_json(data, output):
    print(f"Salvando em {output}")
    with open(output, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    save_to_json(bridge_pokemon_habilidade, bridge_pokemon_habilidade_PATH)
