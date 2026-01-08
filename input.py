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

#choice
def ask_yes_no(prompt: str) -> bool:
    while True:
        choice = input(prompt).strip().lower()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            return False
        else:
            print("> Invalid input. Please enter 'yes' or 'no'.")

def get_choice(prompt: str, options: list[str]) -> str:
    options_str = "/".join(options)
    while True:
        choice = input(f"{prompt} ({options_str}): ").strip()
        if choice in options:
            return choice
        else:
            print(f"> Invalid input. Please choose from: {options_str}.")


def ask_still_playing() -> bool:
    return ask_yes_no(f"{Fore.YELLOW}> Do you want to continue playing? (yes/no): {Style.RESET_ALL}")
