import json
from pathlib import Path

def save_to_json(data, output: Path):
    """Salva os dados num arquivo json, garantindo a criação do diretório"""
    output.parent.mkdir(parents=True, exist_ok=True)

    with open(output, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Dados salvos em {output}")