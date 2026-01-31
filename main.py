from display import show_display, show_inventory, show_realm_info
from colorama import Fore, Style, Back
import time
import random
import sys
from Player import Player
from Tile import Tile
from input import ask_choice
from player_data import save_data

level_per_round = {
    1: 20, # 0 - 20
    2: 40, # 20 - 40
    3: 60, # 40 - 60
    4: 80, # 60 - 80
    5: 100 # 80 - 100
}

realms = ["Ice Realm", "Fire Realm", "Shadow Realm", "Space Realm", "Void Realm"]

def filter_available_realms(player: Player):
    available_realms = []
    for realm in realms:
        if realm not in player.realm_used:
            available_realms.append(realm)
    return available_realms


def main():
    player = Player()
    tile = Tile(player)

    for current_round in range(1, 6):

        while player.level < level_per_round[current_round]: 
            if not player.is_alive:
                print(Fore.MAGENTA + "You lost the game!" + Style.RESET_ALL)
                sys.exit()

            
            print(Fore.RED + 'Type (I) for inventory' + Style.RESET_ALL)
            print(Fore.RED + "Type (R) for show current realm's info" + Style.RESET_ALL)

            choice = input(Fore.RED + "Play a game (y/n): " + Style.RESET_ALL)

            if choice == "y":
                show_display(player, tile, current_round) # 1. show first display
                time.sleep(3)

                print(Back.YELLOW + "Rolling the dice..." + Style.RESET_ALL)
                time.sleep(4)

                dice = random.randint(1, 6)
                print(Fore.YELLOW + f"Your got dice: {dice}" + Style.RESET_ALL)
                time.sleep(1)

                player.change_level(+dice)
                player.change_position(+dice)

                # if he gets 20 or 21 levels, that means he finished round 1  and need to start from level 20 in round 2
                if player.level > level_per_round[current_round]:
                    player.set_level(level_per_round[current_round])

                if player.position > level_per_round[current_round]:
                    player.change_position(level_per_round[current_round])

                show_display(player, tile, current_round) # 2. show after rolling dice

                tile.generate_magic(player.level)
                time.sleep(3)
                show_display(player, tile, current_round) # 3. show after generating magic

                save_data(player)
            elif choice == "I":
                show_inventory(player)
            elif choice == "R":
                show_realm_info(player)
            elif choice == "n":
                sys.exit()
            else:
                print("Please answer with valid input")
                
        player.set_level(level_per_round[current_round]) # restart the player level for next round start level
        player.position = 0  # chnage the position to 0, so it will make to the start 
        print(Fore.GREEN + f"=== Round {current_round} finished! ===" + Style.RESET_ALL)
        time.sleep(2)

        # if the player has next_realm already, set it to current_realm otherwise ask for choice
        if player.next_realm:
            player.current_realm = player.next_realm
            player.realm_used.append(player.next_realm)
            player.next_realm = None
        else:
            availabel_realms = filter_available_realms(player)
            realm_choice = ask_choice(f"{Back.CYAN}Choose the next realm{Style.RESET_ALL}", availabel_realms)
            print(Fore.CYAN + f"You have chosen the realm for round {current_round + 1}: {realm_choice}" + Style.RESET_ALL)
            player.realm_used.append(realm_choice)
            player.current_realm = realm_choice


    print(Fore.MAGENTA + "Congrulation! You have completed all 5 rounds" + Style.RESET_ALL)

main()