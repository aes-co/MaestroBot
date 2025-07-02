import yaml
import os

def load_strings(lang="en"):
    path = os.path.join(os.path.dirname(__file__), f"{lang}.yml")
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)