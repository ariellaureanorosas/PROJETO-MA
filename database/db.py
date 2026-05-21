import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "produtos.json")


def carregar_dados():
    if not os.path.exists(DB_PATH):
        salvar_dados([])
        return []
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_dados(dados):
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)
