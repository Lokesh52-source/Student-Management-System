import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "student.json"


def save_data(students):
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)


def load_data():

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []