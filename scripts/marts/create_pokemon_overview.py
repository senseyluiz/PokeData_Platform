import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

OUTPUT_PATH = BASE_DIR / "data/marts/pokemon_overview.csv"

# Ler arquivos processados
df_pokemon = pd.read_json(BASE_DIR / "data/processed/dim_pokemon.json")
df_stats = pd.read_json(BASE_DIR / "data/processed/fato_pokemon_stats.json")
df_bridge = pd.read_json(BASE_DIR / "data/processed/bridge_pokemon_tipo.json")
df_tipo = pd.read_json(BASE_DIR / "data/processed/dim_tipo.json")

# JOINS
df = df_pokemon.merge(df_stats, on="id_pokemon")
df = df.merge(df_bridge, on="id_pokemon")
df = df.merge(df_tipo, on="id_tipo")

# Criar score
df["score"] = round((
    df["attack"] * 0.3 +
    df["special_attack"] * 0.2 +
    df["speed"] * 0.2 +
    df["hp"] * 0.1 +
    df["defense"] * 0.1 +
    df["special_defense"] * 0.1
), 2)

# Selecionar colunas
df_final = df[
    [
        "id_pokemon",
        "nome_pokemon",
        "nome_tipo",
        "hp",
        "attack",
        "defense",
        "speed",
        "score",
        "url_imagem"
    ]
]

# Criar pasta
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

# Exportar CSV
df_final.to_csv(OUTPUT_PATH, index=False)

print(f"✅ Mart criada em: {OUTPUT_PATH}")