from colorama import Fore, Style
import json
import os

DATA_FILE = "players.json"

#create player JSON
def load_players():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_players(players):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(players, f, indent=4)


#player data
def find_player(players, name, id):
    for p in players:
        if p["name"] == name and p["id"] == id:
            return p
    return None


def create_player(name, id):
    return {
        "name": name,
        "id": id,
        "score": 0,
        "level": 1
    }
