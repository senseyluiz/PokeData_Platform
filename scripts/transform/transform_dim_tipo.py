import pandas as pd
import json
from pathlib import Path

from scripts.utils.file_utils import save_to_json

BASE_DIR = Path(__file__).resolve().parents[2]
OUTPUT_PATH = BASE_DIR / "data/processed/"

dim_tipo_OUTPUT_PATH = OUTPUT_PATH / "dim_tipo.json"

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


if __name__ == "__main__":
    save_to_json(dim_tipo, dim_tipo_OUTPUT_PATH)