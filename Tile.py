from input import ask_choice, ask_yes_no
from colorama import Style, Back, Fore
import random
from Player import Player
import time

class Tile:
    def __init__(self, player: Player):
        self.player = player
        self.tiles = self.generate_tiles()

    def generate_tiles(self):
        base_tiles = [
            "Card",
            "Enemy",
            "Trap",
            "Mystery",
            "Shop",
            "Portal",
            "Realm",
            "Treasure",
            'Cursed',
            'Altar'
        ]
        return random.choices(base_tiles, k=20)

    def card_tile(self):
        choice = ask_choice("Choose One", ["Health", "Defense", "Coin"])
        if choice == "Health":
            self.player.change_health(+5)
            print(Fore.CYAN + f"Health: +5 hp" + Style.RESET_ALL)
        elif choice == "Defense":
            self.player.add_defense_cards(+1)
            print(Fore.CYAN + f"Defense: +1 defense card" + Style.RESET_ALL)
        else:
            if self.player.current_realm == "Fire Realm":
                self.player.change_coins(+7)
                print(Fore.CYAN + f"Coin: +7 coins (Fire Realm)" + Style.RESET_ALL)
            else:
                self.player.change_coins(+5)
                print(Fore.CYAN + f"Coin: +5 coins" + Style.RESET_ALL)

            

    def enemy_tile(self):
        if self.player.inventory["Tank magic"] > 0:
           num_tank_magic = self.player.inventory["Tank magic"]
           choice = ask_yes_no(f"You have Tank magic ({num_tank_magic}). Do you want to use? (y/n): ")
           if choice:
               print(Fore.CYAN + "You have used Tank magic. No enemy attack." + Style.RESET_ALL)
               return

        if self.player.current_realm == "Shadow Realm":
            num_defense_cards = 0
            print(Fore.CYAN + "Shadow Trap: Defense cards cannot be used in the Shadow Realm!" + Style.RESET_ALL)
        else:
            num_defense_cards = self.player.defense_cards

        dmg = 2 if self.player.current_realm == "Ice Realm" else 0

        print(Fore.CYAN + f"Choosing an enemy..." + Style.RESET_ALL)
        time.sleep(3)

        enemy_rank = random.choice(["Elite", "Master", "Epic"])

        if enemy_rank == "Elite":
            print(Fore.CYAN + f"You got Elite rank" + Style.RESET_ALL)
            if num_defense_cards >= 1:
                use = ask_yes_no(Fore.CYAN + f"You have {num_defense_cards} defense cards. Do you want to use? (y/n): " + Style.RESET_ALL)
                if use:
                    if self.player.current_realm == "Fire Realm":
                        print(Fore.CYAN + "You have defeated Elite Rank. You gained +1 level bonus. (Fire Realm)" + Style.RESET_ALL)
                        self.player.change_level(+1)
                        self.player.change_position(+1)

                    self.player.add_defense_cards(-1)
                    return
            else:
                enemy_type = random.choice(["Zombie", "Werewolf"])
                print(Fore.CYAN + f"You got {enemy_type} ({enemy_rank} rank)" + Style.RESET_ALL)
                time.sleep(2)
                if enemy_type == "Zombie":
                    total = 3 + dmg
                    self.player.change_health(-total)
                    print(Fore.CYAN + f"Zombie: -{total} hp" + Style.RESET_ALL)
                    time.sleep(2)
                else:
                    total = 2 + dmg
                    self.player.change_health(-total)
                    self.player.change_level(-1)
                    self.player.change_position(-1)
                    print(Fore.CYAN + f"Werewolf: -{total} hp and -1 level" + Style.RESET_ALL)
                    time.sleep(2)

        elif enemy_rank == "Master":
            print(Fore.CYAN + f"You got Master rank" + Style.RESET_ALL)
            if num_defense_cards >= 2:
                use = ask_yes_no(Fore.CYAN + f"You have {num_defense_cards} defense cards. Do you want to use? (y/n): " + Style.RESET_ALL)
                if use:
                    if self.player.current_realm == "Fire Realm":
                        print(Fore.CYAN + "You have defeated Master Rank. You gained +1 level bonus. (Fire Realm)" + Style.RESET_ALL)
                        self.player.change_level(+1)
                        self.player.change_position(+1)

                    self.player.add_defense_cards(-2)
                    return
            else:
                enemy_type = random.choice(["Vampire", "Demon"])
                print(Fore.CYAN + f"You got {enemy_type} ({enemy_rank} rank)" + Style.RESET_ALL)
                time.sleep(2)
                if enemy_type == "Vampire":
                    total = 4 + dmg
                    self.player.change_health(-total)
                    print(Fore.CYAN + f"Vampire: -{total} hp" + Style.RESET_ALL)
                    time.sleep(2)
                else:
                    total = 3 + dmg
                    self.player.change_health(-total)
                    self.player.change_level(-1)
                    self.player.change_position(-1)
                    print(Fore.CYAN + f"Demon: -{total} hp and -1 level" + Style.RESET_ALL)
                    time.sleep(2)

        elif enemy_rank == "Epic":
            print(Fore.CYAN + f"You got Epic rank" + Style.RESET_ALL)
            if num_defense_cards >= 3:
                use = ask_yes_no(Fore.CYAN + f"You have {num_defense_cards} defense cards. Do you want to use? (y/n): " + Style.RESET_ALL)
                if use:
                    if self.player.current_realm == "Fire Realm":
                        print(Fore.CYAN + "You have defeated Epic Rank. You gained +1 level bonus." + Style.RESET_ALL)
                        self.player.change_level(+1)
                        self.player.change_position(+1)

                    self.player.add_defense_cards(-3)
                    return
            else:
                enemy_type = random.choice(["Dragon", "Beast"])
                print(Fore.CYAN + f"You got {enemy_type} ({enemy_rank} rank)" + Style.RESET_ALL)
                time.sleep(2)
                if enemy_type == "Dragon":
                    total = 5 + dmg
                    self.player.change_health(-total)
                    print(Fore.CYAN + f"Dragon: -{total} hp" + Style.RESET_ALL)
                    time.sleep(2)
                else:
                    total = 4 + dmg
                    self.player.change_health(-total)
                    self.player.change_level(-1)
                    self.player.change_position(-1)
                    print(Fore.CYAN + f"Beast: -{total} hp and -1 level" + Style.RESET_ALL)
                    time.sleep(2)


    def trap_tile(self):
        if self.player.current_realm == "Void Realm":
            self.player.change_health(-3)
            self.player.change_level(-3)
            self.player.change_position(-3)
            print(Fore.CYAN + "Trap: -3 hp and -3 level (Void Realm)" + Style.RESET_ALL)
            return

        if self.player.current_realm == "Ice Realm":
            self.player.change_level(-5)
            self.player.change_position(-5)
            print(Fore.CYAN + "Trap: -5 levels (Ice Realm)" + Style.RESET_ALL)
        else:
            result = random.choice(["HP", "Level"])
            if result == "HP":
                self.player.change_health(-5)
                print(Fore.CYAN + "HP: -5 hp" + Style.RESET_ALL)
            else:
                self.player.change_level(-5)
                self.player.change_position(-5)
                print(Fore.CYAN + "Level: -5 levels" + Style.RESET_ALL)


    def mystery_tile(self):
        print(Fore.CYAN + "Choosing your luck..." + Style.RESET_ALL)
        luck = random.choice(["bad", "good"])
        print(Fore.CYAN + f"Your luck is {luck}" + Style.RESET_ALL)
        time.sleep(2)

        if luck == "bad":
            self.player.change_health(-5)
            self.player.change_level(-2)
            self.player.change_position(-2)
            print(Fore.CYAN + "Bad luck: -5 hp and -2 level" + Style.RESET_ALL)
        else:
            self.player.change_coins(+5)
            self.player.change_level(+3)
            self.player.change_position(+3)
            print(Fore.CYAN + "Good luck: +5 coins and +3 level" + Style.RESET_ALL)

    def shop_tile(self):
        choice = ask_choice(
            """
                Items available
                (i) Health magic (-1 coin) = +5 hp
                (ii) Tank magic (-2 coins) = can defense any enemy of rank
                (iii) Time magic (-3 coins) = can move +5 levels
                (iv) Immune magic (-4 coins) = can skip any cell  once
                (v) Gold magic (-5 coins)= +10 coins
                (vi) Exit the shop
            """,
            ["i", "ii", "iii", "iv", "v", "vi"]
        )

        if choice == "i":
            if self.player.coins >= 1:
                print(Fore.CYAN + "Health magic: +5 hp" + Style.RESET_ALL)
                self.player.change_health(+5)
                self.player.change_coins(-1)
            else:
                print(Fore.CYAN + "Not enough coins" + Style.RESET_ALL)
        elif choice == "ii":
            if self.player.coins >= 2:
                print(Fore.CYAN + "Tank magic added: can defense any enemy" + Style.RESET_ALL)
                self.player.inventory["Tank magic"] += 1
                self.player.change_coins(-2)
            else:
                print(Fore.CYAN + "Not enough coins" + Style.RESET_ALL)
        elif choice == "iii":
            if self.player.coins >= 3:
                if self.player.current_realm == "Space Realm":
                    self.player.change_level(+7)
                    self.player.change_position(+7)
                    print(Fore.CYAN + "Time magic: +7 levels (Space Realm)" + Style.RESET_ALL)
                    self.player.change_coins(-3)
                else:
                    self.player.change_level(+5)
                    self.player.change_position(+5)
                    print(Fore.CYAN + "Time magic: +5 level" + Style.RESET_ALL)
                    self.player.change_coins(-3)
            else:
                print(Fore.CYAN + "Not enough coins" + Style.RESET_ALL)
        elif choice == "iv":
            if self.player.coins >= 4:
                amount = 2 if self.player.current_realm == "Void Realm" else 1
                self.player.inventory["Immune magic"] += amount
                print(Fore.CYAN + f"{amount} Immune magic added: can skip any cell once" + Style.RESET_ALL)
                self.player.change_coins(-4)
            else:
                print(Fore.CYAN + "Not enough coins" + Style.RESET_ALL)
        elif choice == "v":
            if self.player.coins >= 5:
                self.player.change_coins(+10)
                print(Fore.CYAN + "Gold magic: +10 coins" + Style.RESET_ALL)
                self.player.change_coins(-5)
            else:
                print(Fore.CYAN + "Not enough coins" + Style.RESET_ALL)
        else:
            return

    def portal_tile(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        direction = "forward" if dice1 % 2 == 0 or self.player.current_realm == "Space Realm" else "backward"
        step = dice2        
        if direction == "forward":
            self.player.change_level(+step)
            self.player.change_position(+step)
        else:
            self.player.change_level(-step)
            self.player.change_position(-step)  
            
        print(Fore.CYAN + f"You move {step} ({direction})" + Style.RESET_ALL)


    def realm_tile(self):
        choice = ask_choice("Choose next realm", ["Ice Realm", "Fire Realm", "Shadow Realm", "Space Realm", "Void Realm"])
        self.player.next_realm = choice

    def treasure_cell(self):
        choice = ask_choice(
            """
            Choose one
            (i) Gemstone = +6 coins
            (ii) Ancient scroll = +3 defense cards
            (iii) Mystic portion = +3 hp and +1 level
            """,
            ["i", "ii", "iii"]
        )     

        if choice == "i":
            self.player.change_coins(+6)
            print(Fore.CYAN + "Gemstone: +6 coins" + Style.RESET_ALL)
        elif choice == "ii":
            self.player.add_defense_cards(+3)
            print(Fore.CYAN + "Ancient scroll: +3 defense cards" + Style.RESET_ALL)
        else:
            self.player.change_health(+3)
            self.player.change_level(+1)
            self.player.change_position(+1)
            print(Fore.CYAN + "Mystic portion: +3 hp and +1 level" + Style.RESET_ALL)
    
    def cursed_tile(self):
        choice = ask_choice(
            """
            Choose one
            (i) Weakness curse = -2 defense cards
	        (ii) Decay curse = -3 hp and -2 coins

            """,
            ["i", "ii"]
        )     

        if choice == "i":
            self.player.add_defense_cards(-2)
            print(Fore.CYAN + "Weakness curse: -2 defense cards" + Style.RESET_ALL)
        else:
            self.player.change_health(-3)
            self.player.change_coins(-2)
            print(Fore.CYAN + "Decay curse: -3 hp and -2 coins" + Style.RESET_ALL)
            

    def altar_cell(self):
        choice = ask_choice(
            """
            Choose one
            (i) Sacrifice Coins = Lose 5 coins, gain +2 defense cards
	        (ii) Sacrifice HP = Lose 3 hp, gain +5 levels
	        (iii) Sacrifice Levels = Lose 2 levels, gain +5 coins
            """,
            ["i", "ii", "iii"]
        )     

        if choice == "i":
            self.player.change_coins(-5)
            self.player.add_defense_cards(+2)
            print(Fore.CYAN + "Sacrifice Coins = -5 coins but +2 defense cards" + Style.RESET_ALL)
        elif choice == "ii":
            self.player.change_health(-3)
            self.player.change_level(+5)
            self.player.change_position(+5)
            print(Fore.CYAN + "Sacrifice Hp = -3 hp but +5 levels" + Style.RESET_ALL)
        else:
            self.player.change_level(-2)
            self.player.change_position(-2)
            self.player.change_coins(+5)
            print(Fore.CYAN + "Sacrifice Levels = -2 levels but +5 coins" + Style.RESET_ALL)


    def generate_magic(self, level):
        if level == 0:
            return
        
        # if level beyound 20, we will get error, so modify levels for every round 
        tile_index = (level - 1) % len(self.tiles)
        tile_name = self.tiles[tile_index]
        print(Back.CYAN + f"You landed on {tile_name}" + Style.RESET_ALL)

        if self.player.current_realm == "Shadow Realm" and tile_name == "Mystery":
            print(Fore.CYAN + "The Shadow Realm forbids skipping Mystery tiles!" + Style.RESET_ALL)
            self.mystery_tile()
            return

        num_immune_magic = self.player.inventory["Immune magic"]
        if num_immune_magic > 0:
            use = ask_yes_no(Fore.CYAN + f"You have {num_immune_magic} Immune magic. Use? (y/n): " + Style.RESET_ALL)
            if use:
                self.player.inventory["Immune magic"] -= 1
                print(Fore.CYAN + f"You have skipped {tile_name}" + Style.RESET_ALL)
                return
    
        if tile_name == "Card":
            self.card_tile()
        elif tile_name == "Enemy":
            self.enemy_tile()
        elif tile_name == "Trap":
            self.trap_tile()
        elif tile_name == "Mystery":
            self.mystery_tile()
        elif tile_name == "Shop":
            self.shop_tile()
        elif tile_name == "Portal":
            self.portal_tile()
        elif tile_name == "Realm":
            self.realm_tile()
        elif tile_name == "Treasure":
            self.treasure_cell()
        elif tile_name == "Cursed":
            self.cursed_tile()
        elif tile_name == "Altar":
            self.altar_cell()
        else:
            print("Unknown tile. No effect.")

