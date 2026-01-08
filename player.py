health = 0
coins = 0
level = 0
is_alive = True
defense_cards = 0

def add_health(amount):
    health += amount
    if health < 0:
        is_alive = False
    
def add_coins(amount):
    coins += amount
    if coins < 0:
        coins = 0

def change_level(amount):
    level += amount
    if level < 0:
        level = 0

def add_defense_cards(amount):
    defense_cards += amount
