import pandas as pd
import json
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUTPUT_PATH = os.path.join(BASE_DIR, "data/processed/habilidade.json")

abilitie_PATH = os.path.abspath(os.path.join(BASE_DIR, "data/lake/raw/abilities.json"))

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
    print(f"Salvando em {OUTPUT_PATH}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    save_habilidade_to_json(dim_habilidade)

