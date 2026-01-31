import json
import os
from datetime import datetime;
from Player import Player

DATA_FILE = "players.json"

def save_data(player: Player):
    player_data = {
        "health": player.health,
        "coin": player.coins,
        "level": player.level,
        "position": player.position,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "realm": player.current_realm
    }

    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    data.append(player_data)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)