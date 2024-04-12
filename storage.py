import json
import os

STORAGE_FILE = 'kanban_data.json'

def load_data():
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, 'r') as file:
            return json.load(file)
    return {"boards": []}

def save_data(data):
    with open(STORAGE_FILE, 'w') as file:
        json.dump(data, file, indent=4)
