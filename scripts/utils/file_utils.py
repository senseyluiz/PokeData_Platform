import json
from pathlib import Path
import pandas as pd

def save_to_json(data, output: Path):
    """Salva os dados num arquivo json, garantindo a criação do diretório"""
    output.parent.mkdir(parents=True, exist_ok=True)

    with open(output, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Dados salvos em {output}")


def load_table(conn, df, table_name):
    """Carrega os dados na tabela onde:
        conn = engine de conexão com o banco de dados
        df = os dados vindo da tabela transformada,
        table_name = nome da tabela a ser carregada"""
    from sqlalchemy import text
    print(f"\n🔄 Carregando tabela: {table_name}")
    conn.execute(text(f"TRUNCATE TABLE {table_name} CASCADE"))
    df.to_sql(table_name, con=conn, if_exists='append', index=False)
    print(f"\33[32m✔ {table_name} carregada com sucesso!\33[0m")


def load_json_to_df(path: Path) -> pd.DataFrame:
    """
    Lê um arquivo JSON e retorna um DataFrame
    """
    print(f"📥 Lendo arquivo: {path}")

    df = pd.read_json(path)

    print(f"\33[32m✔ DataFrame carregado: {len(df)} registros\33[0m")

    return df