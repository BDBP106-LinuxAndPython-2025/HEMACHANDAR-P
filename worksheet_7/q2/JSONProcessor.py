# JSONProcessor.py
import json

def load_json(filepath):
    """Load JSON data into a Python object."""
    with open(filepath, "r") as f:
        data = json.load(f)
    return data

def print_json(data):
    """Pretty-print JSON data."""
    print(json.dumps(data, indent=4))

def update_man_of_the_match(data):
    """Set man_of_the_match to True for the player with max score."""
    max_score = max(player["player_score"] for player in data)
    for player in data:
        player["man_of_the_match"] = (player["player_score"] == max_score)
    return data

def write_json(filepath, data):
    """Write updated JSON data to a new file."""
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
