from urllib.parse import quote_plus

from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

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
    with engine.connect() as conn:
        print("\33[32mConexão bem sucedida!\33[0m")
        sql = text("SELECT * FROM dim_tipo")
        result = conn.execute(sql)
        print(result.fetchall())
except Exception as e:
    print(f"\33[31mFalha na conexão: {e}\33[m")
