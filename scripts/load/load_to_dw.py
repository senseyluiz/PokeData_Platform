from urllib.parse import quote_plus
import pandas as pd
from pathlib import Path

from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
BASE_DIR = Path(__file__).resolve().parents[2]

dim_tipo = pd.read_json(BASE_DIR / "data/processed/dim_tipo.json")
df_dim_tipo = pd.DataFrame(dim_tipo)


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
        conn.execute(text("DELETE FROM dim_tipo"))
        df_dim_tipo.to_sql("dim_tipo", con=conn, if_exists='append', index=False)
        print("\33[32m✔ Dados inseridos com sucesso!\33[0m")

except Exception as e:
    print(f"\33[31m✘ Falha na conexão: {e}\33[m")
