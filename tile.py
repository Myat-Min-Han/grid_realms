from input import ask_choice
from player import add_health, add_coins, change_level, add_defense_cards, context, coins, next_realm, current_realm
import random

def card_tile():
    if "Space Realm" in current_realm:
        print(">>> You cannot pick the cards in Space Realm")
        return
    
    choice: str = ask_choice("Choose from these cards", ["Health", "Coins", "Defense"])
    if choice == "Health":
        add_health(+5)
    elif choice == "Coins":
        add_coins(+5)
    elif choice == "Defense":
        add_defense_cards(1)

def enemy_tile():
    enemy_rank = random.choice(["Normal", "Elite", "Boss"])
    c_damage = 2 if "Fire Realm" in current_realm else 0

    if enemy_rank == "Normal":
        enemy_type = random.choice(["Monster", "Werewolf"])
        if enemy_type == "Monster":
            add_health(-2 + c_damage)
        elif enemy_type == "Werewolf":
            add_health(-1 + c_damage)
            change_level(-1)
    elif enemy_rank == "Elite":
        enemy_type = random.choice(["Demon", "Beast"])
        if enemy_type == "Demon":
            add_health(-4 + c_damage)
        elif enemy_type == "Beast":
            change_level(-3)
    elif enemy_rank == "Boss":
        enemy_type = random.choice(["Shadow King", "Vampire"])
        if enemy_type == "Shadow King":
            add_health(-5 + c_damage)
        elif enemy_type == "Vampire":
            add_health(-3 + c_damage)
            change_level(-2)

def trap_tile():
    choice = random.choice(["Health", "Level"])
    c_damage = 1 if "Shadow Realm" in current_realm else 0

    if choice == "Health":
        add_health(-5 - c_damage)
    elif choice == "Level":
        change_level(-2 - c_damage)

def mystery_tile():
    if "Void Realm" in current_realm:
        print(">>> Always bad luck in Void Realm")
        change_level(-5)
        return 
    
    luck = random.choice(["good", "bad"])
    if luck == "good":
        add_health(+3)
        add_coins(+4)
    elif luck == "bad":
        change_level(-5)

def special_tile():
    choice = random.choice(["King", "Queen", "Joker"])
    if choice == "King":
        change_level(+9)
    elif choice == "Queen":
        change_level(+6)
    elif choice == "Joker":
        add_health(-5)
        add_coins(-2)

def event_tile():
    choice = ask_choice("Please choose one of these 3 cards", ["1", "2", "3"])
    # phase 1
    if choice == "1":
        choice = ask_choice("Please choose -4 hp or -2 levels", ["hp", "level"])
        if choice == "hp":
            add_health(-4)
        else:
            change_level(-2)
    # phase 2
    if choice == "2":
        choice = ask_choice("Please choose +5 coins or +5 hp", ["coin", "hp"])
        if choice == "coin":
            add_coins(+5)
        else:
            add_health(+5)
    # phase 3
    if choice == "3":
        choice = ask_choice("Please choose to skip Shop Tile or Enemy Tile", ["Shop", "Enemy"])
        if choice == "Shop":
            context["skip_shop_once"] = True
        else:
            context["skip_enemy_once"] = True
        
def portal_tile():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    direction = "forward" if dice1 % 2 == 0 else "backward"
    step = dice2
    print(f">>> You get {step}{direction}")
    change_level(+step)

def shop_tile():
    # check coins
    if coins <= 0:
        print(">>> Not enough coins")
        return

    choice = ask_choice(
        """
            Please choose item from shop
            (1) Health portion(-1 coin) - +5 hp, 
            (2) Lucky key(-2 coins) - can skip a Trap Tile once, 
            (3) Mystery key(-3 coin) - can skip a mystery tile once,
            (4) Immune magic(-4 coins) - can defense any rank of enemy rank , 
            (5) Vow scroll(-5 coins) - can skip +3 levels but will reduce -3 hp
        """,
        ["1", "2", "3", "4", "5"]
    )

    if choice == "1":
        add_health(+5)
        add_coins(-1)
    elif choice == "2":
        context["skip_trap_once"] = True
        add_coins(-2)
    elif choice == "3":
        context["skip_mystery_once"] = True
        add_coins(-3)
    elif choice == "4":
        context["has_immune_magic"] = True
    else:
        change_level(+3)
        add_health(-3)

def cursed_tile():
    choice = ask_choice("Please chooe +1/-1", ["+1", "-1"])
    dice = random.randint(1, 6)
    if choice == "+1":
        change_level(dice + 1)
    else: 
        change_level(dice - 1)
    
def thief_tile():
    if "Void Realm" in current_realm:
        print(">>> All coins will be stolen in Void Realm")
        coins = 0
        return
    
    stolen = random.randint(1, 6)
    add_coins(-stolen)

def realm_tile():
    choice = ask_choice(
        "Please choose next realm", 
        ["Ice Realm", "Fire Realm", "Shadow Realm", "Space Realm", "Void Realm"])
    next_realm.append(choice)

def wizard_tile():
    if "Space Realm" in current_realm:
        print(">>> You will not get the wizard magic in Space Realm")
        return 
    
    context["has_wizard_magic"] = True

