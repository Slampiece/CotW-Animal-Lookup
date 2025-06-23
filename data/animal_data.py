import json
import os

file_path = os.path.join(os.path.dirname(__file__), "animals_clean_export.json")

with open(file_path, "r", encoding="utf-8") as f:
    raw_animals = json.load(f)

# Convert list into dictionary where the key is the lowercase animal name
animals = {
    entry['animal_name'].lower(): entry
    for entry in raw_animals
    if 'animal_name' in entry and entry['animal_name'].strip() != ""
}

