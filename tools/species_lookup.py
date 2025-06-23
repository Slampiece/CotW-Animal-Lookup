import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rapidfuzz import process
from data.animal_data import animals

def find_animal(query):
    query = query.lower().strip()
    all_animals = list(animals.keys())

    # 1. Exact match
    if query in animals:
        return query, animals[query]

    # 2. Fuzzy match
    match = process.extractOne(query, all_animals, score_cutoff=60)
    if match:
        best_name = match[0]
        return best_name, animals[best_name]

    # 3. Not found
    return None, None
