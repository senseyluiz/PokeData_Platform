import pandas as pd
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
OUTPUT_PATH = BASE_DIR / "data/processed/"

dim_tipo_PATH = BASE_DIR / "dim_tipo.json"

TYPES_PATH = BASE_DIR / "data/lake/raw/types.json"

df_types = pd.read_json(TYPES_PATH)

list_types = df_types["name"].unique().tolist()
list_types = [tipo for tipo in list_types if not tipo in ["unknown", "shadow"]]
dim_tipo = [
    {
        "id_tipo": i + 1,
        "nome_tipo": tipo
     }
    for i , tipo in enumerate(list_types)
]

# Será utilizado para a tabela bridge_pokemon_tipo
tipo_map = {tipo: i + 1 for i, tipo in enumerate(list_types)}

def save_tipo_to_json(data):
    print(f"Salvando em {dim_tipo_PATH}")
    with open(dim_tipo_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    save_tipo_to_json(dim_tipo)