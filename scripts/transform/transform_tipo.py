import pandas as pd
import json
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUTPUT_PATH = os.path.join(BASE_DIR, "data/processed/tipo.json")
TYPES_PATH = os.path.join(BASE_DIR, "data/lake/raw/types.json")

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

tipo_map = {tipo: i + 1 for i, tipo in enumerate(list_types)}

def save_tipo_to_json(data):
    print(f"Salvando em {OUTPUT_PATH}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    save_tipo_to_json(dim_tipo)