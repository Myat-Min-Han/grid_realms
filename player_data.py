import json
import os

DATA_FILE = "players.json"

def load_all_data():
    """Read the entire JSON file. Create it if missing."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save_all_data(players_list):
    """Overwrite the JSON file with the current list."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(players_list, f, indent=4)

def find_player_in_db(name):
    """Check if a name exists and return its data."""
    db = load_all_data()
    for p in db:
        if p["name"].lower() == name.lower():
            return p
    return None

def save_or_update_db(player_obj):
    """Sync the Player object data back to the JSON file."""
    db = load_all_data()
    # Prepare the data dictionary from the object
    new_data = {
        "name": player_obj.name,
        "health": player_obj.health,
        "coin": player_obj.coin,
        "level": player_obj.level,
        "realm": player_obj.realm
    }
    
    found = False
    for i in range(len(db)):
        if db[i]["name"].lower() == player_obj.name.lower():
            db[i] = new_data # Update existing
            found = True
            break
    
    if not found:
        db.append(new_data) # Add new
    
    save_all_data(db)