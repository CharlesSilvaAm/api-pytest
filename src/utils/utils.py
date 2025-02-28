import json
import os

def load_json(filepath):
    """Carrega e retorna dados de um arquivo JSON."""
    base_dir = os.path.dirname(os.path.abspath(__file__))  
    full_path = os.path.join(base_dir, "..", filepath)  
    with open(full_path, "r", encoding="utf-8") as file:
        return json.load(file)