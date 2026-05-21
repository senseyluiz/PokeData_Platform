import pandas as pd
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parents[2]
OUTPUT_PATH = BASE_DIR / "data/processed/"

dim_habilidade_path = OUTPUT_PATH / "dim_habilidade.json"

abilitie_PATH = BASE_DIR / "data/lake/raw/abilities.json"

df_abilities = pd.read_json(abilitie_PATH)

list_abilities = df_abilities["name"].unique().tolist()
list_abilities = [abilitie for abilitie in list_abilities if abilitie not in ["unknown", "shadow"]]
dim_habilidade = [
    {
        "id_habilidade": i + 1,
        "nome_habilidade": nome
    }
    for i, nome in enumerate(list_abilities)
]

# Será utilizado para mapear a tabela bridge_pokemon_habilidade
habilidade_map = {habilidade: i + 1 for i, habilidade in enumerate(list_abilities)}

def save_habilidade_to_json(data):
    print(f"Salvando em {dim_habilidade_path}")
    with open(dim_habilidade_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    save_habilidade_to_json(dim_habilidade)

