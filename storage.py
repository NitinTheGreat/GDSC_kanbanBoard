import json
import os

STORAGE_FILE = 'kanban_data.json'

def load_data():
    # Initialize data as a dictionary with key "boards"
    data = {"boards": {}}
    
    # Check if the storage file exists
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, 'r') as file:
            file_data = json.load(file)
            if isinstance(file_data, dict):
                data = file_data
            else:
                # Handle the case where the file data is not a dictionary
                data = {"boards": {}}
                
    return data

def save_data(data):
    with open(STORAGE_FILE, 'w') as file:
        json.dump(data, file, indent=4, default=lambda o: o.__dict__)


