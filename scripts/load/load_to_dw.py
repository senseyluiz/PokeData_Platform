from urllib.parse import quote_plus
from pathlib import Path

from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

from scripts.utils.file_utils import load_table, load_json_to_df

BASE_DIR = Path(__file__).resolve().parents[2]

df_dim_tipo = load_json_to_df(BASE_DIR / "data/processed/dim_tipo.json")
df_dim_habilidade = load_json_to_df(BASE_DIR / "data/processed/dim_habilidade.json")
df_dim_pokemon = load_json_to_df(BASE_DIR / "data/processed/dim_pokemon.json")
df_bridge_pokemon_tipo = load_json_to_df(BASE_DIR / "data/processed/bridge_pokemon_tipo.json")
df_bridge_pokemon_habilidade = load_json_to_df(BASE_DIR / "data/processed/bridge_pokemon_habilidade.json")
df_fato_pokemon_stats = load_json_to_df(BASE_DIR / "data/processed/fato_pokemon_stats.json")

# Configurações de conexão
load_dotenv()
HOST = os.getenv("DB_HOST")
USER = os.getenv("DB_USER")
PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))
PORT = os.getenv("DB_PORT")
DBNAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

engine = create_engine(DATABASE_URL)

try:
    with engine.begin() as conn:
        print("\33[32m✔ Conexão bem sucedida!\33[0m")
        load_table(conn, df_dim_tipo, "dim_tipo")
        load_table(conn, df_dim_habilidade, "dim_habilidade")
        load_table(conn, df_dim_pokemon, "dim_pokemon")
        load_table(conn, df_fato_pokemon_stats, "fato_pokemon_stats")
        load_table(conn, df_bridge_pokemon_tipo, "bridge_pokemon_tipo")
        load_table(conn, df_bridge_pokemon_habilidade, "bridge_pokemon_habilidade")

except Exception as e:
    print(f"\33[31m✘ Falha na conexão: {e}\33[m")
