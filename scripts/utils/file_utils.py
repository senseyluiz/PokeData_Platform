import json
from pathlib import Path

def save_to_json(data, output: Path):
    """Salva os dados num arquivo json, garantindo a criação do diretório"""
    output.parent.mkdir(parents=True, exist_ok=True)

    with open(output, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Dados salvos em {output}")


def load_table(conn, df, table_name):
    from sqlalchemy import text
    print(f"\n🔄 Carregando tabela: {table_name}")
    conn.execute(text(f"TRUNCATE TABLE {table_name} CASCADE"))
    df.to_sql(table_name, con=conn, if_exists='append', index=False)
    print(f"\33[32m✔ {table_name} carregada com sucesso!\33[0m")