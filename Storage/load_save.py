import json

file_path = 'garage.json'

def read():
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print('No File Found, Continuing with empty list.')
        return []  
    except json.JSONDecodeError:
        print('Error decoding JSON. Continuing with empty list.')
        return []  

def save(my_garage):
    try:
        with open(file_path, 'w') as file:
            json.dump(my_garage, file, indent=4)
    except Exception as e:
        print("Error saving data")
