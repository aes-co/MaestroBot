import yaml

def load_strings(lang: str = "id"):
    with open(f"strings/{lang}.yml", encoding="utf-8") as f:
        return yaml.safe_load(f)

STRINGS = load_strings()
