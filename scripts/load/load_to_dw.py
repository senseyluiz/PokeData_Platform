from urllib.parse import quote_plus
import pandas as pd
from pathlib import Path

from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
BASE_DIR = Path(__file__).resolve().parents[2]

# Ler json de dim_tipo
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

def load_table(conn, df, table_name):
    print(f"\n🔄 Carregando tabela: {table_name}")
    conn.execute(text(f"TRUNCATE TABLE {table_name} CASCADE"))
    df.to_sql(table_name, con=conn, if_exists='append', index=False)
    print(f"\33[32m✔ {table_name} carregada com sucesso!\33[0m")

try:
    with engine.begin() as conn:
        print("\33[32m✔ Conexão bem sucedida!\33[0m")
        load_table(conn,df_dim_tipo, "dim_tipo")
except Exception as e:
    print(f"\33[31m✘ Falha na conexão: {e}\33[m")
