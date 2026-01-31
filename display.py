from Player import Player
from colorama import Fore, Style, Back
from Tile import Tile

realm_colors = {
    "Ice Realm": Fore.BLUE,
    "Fire Realm": Fore.RED,
    "Shadow Realm": Fore.CYAN,   
    "Space Realm": Fore.MAGENTA,
    "Void Realm": Fore.GREEN
}

realm_info = {
    "Ice Realm": """
        ( Ice Realm )
        - Frost Attack: First enemy attack in this realm deals +2 damage.
        - Frozen Trap: Trap cells only reduce levels, not HP.
    """,
    "Fire Realm": """
        ( Fire Realm )
        - Flame Surge: Every enemy defeated gives +1 level bonus.
        - Burning Coin: Coin cards give +7 coins instead of +5.
    """,
    "Shadow Realm": """
        ( Shadow Realm )
        - Shadow Trap: Defense cards not working on any enemy of rank
        - Dark Bargain: Mystery cells always trigger (no skip).
    """,
    "Space Realm": """
        ( Space Realm )
        - Warp Step: Portal dice rolls always move forward (never backward).
        - Cosmic Leap: Time magic in shop gives +7 levels instead of +5.
    """,
    "Void Realm": """
        ( Void Realm )
        - Void Immunity: Immune magic can be used twice in this realm.
        - Abyssal Trap: Trap cells deal both HP and level loss (-3 HP, -3 levels).
    """
}

def show_inventory(player: Player):
    num_tank_magic = player.inventory["Tank magic"]
    num_immune_magic = player.inventory["Immune magic"]
    num_defense_cards = player.defense_cards
    print(Back.RED + f"Tank magic: {num_tank_magic} | Immune magic: {num_immune_magic} | Defense cards: {num_defense_cards}" + Style.RESET_ALL)


def show_realm_info(player: Player):
    color = realm_colors[player.current_realm]
    realm_data = realm_info[player.current_realm]
    print(color + f"{realm_data}" + Style.RESET_ALL)


def highlight_tile(tile_name, tile_index, player_position):
    if tile_index == player_position:
        return Back.YELLOW + Fore.BLACK + f"{tile_name}" + Style.RESET_ALL
    return f"{tile_name}"


def show_display(player: Player, tile: Tile, current_round):
    tiles =  tile.tiles
    color = realm_colors[player.current_realm]

    tile_display: list[str] = [
        highlight_tile("Start", 0, player.position)
    ] + [
        highlight_tile(tiles[i], i+1, player.position) for i in range(20)
    ]
    # tile_display = [0] + [1 - 20]

    print(
        color + f"""
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    x                                                                                      x
    x ||============|| ||============|| ||============|| ||============|| ||============|| x
    x ||            || ||            || ||            || ||            || ||            || x
    x || {tile_display[0]:>10}  || || {tile_display[1]:>10} || || {tile_display[2]:>10} || || {tile_display[3]:>10} || || {tile_display[4]:>10} || x
    x ||            || ||            || ||            || ||            || ||            || x
    x ||============|| ||============|| ||============|| ||============|| ||============|| x
    x                                                                                   || x
    x                                                                                   \/ x
    x ||============|| ||============|| ||============|| ||============|| ||============|| x
    x ||            || ||            || ||            || ||            || ||            || x
    x || {tile_display[9]:>10} || || {tile_display[8]:>10} || || {tile_display[7]:>10} || || {tile_display[6]:>10} || || {tile_display[5]:>10} || x
    x ||            || ||            || ||            || ||            || ||            || x
    x ||============|| ||============|| ||============|| ||============|| ||============|| x
    x ||                                                                                   x
    x \/                                                                                   x
    x ||============|| ||============|| ||============|| ||============|| ||============|| x
    x ||            || ||            || ||            || ||            || ||            || x
    x || {tile_display[10]:>11}|| || {tile_display[11]:>11}|| || {tile_display[12]:>11}|| || {tile_display[13]:>11}|| || {tile_display[14]:>11}|| x
    x ||            || ||            || ||            || ||            || ||            || x
    x ||============|| ||============|| ||============|| ||============|| ||============|| x
    x                                                                                   || x
    x                                                                                   \/ x
    x ||============|| ||============|| ||============|| ||============|| ||============|| x
    x ||            || ||            || ||            || ||            || ||            || x
    x || {tile_display[19]:>11}|| || {tile_display[18]:>11}|| || {tile_display[17]:>11}|| || {tile_display[16]:>11}|| || {tile_display[15]:>11}|| x
    x ||            || ||            || ||            || ||            || ||            || x
    x ||============|| ||============|| ||============|| ||============|| ||============|| x
    x ||                                                                                   x
    x \/                                                                                   x
    x ||============||                                                                     x
    x ||            ||                                                                     x
    x || {tile_display[20]:>11}||                                                          x
    x ||            ||                                                                     x
    x ||xxxxxxxxxxxx||                                                                     x
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

    HP: {player.health} | Level: {player.level} | Coins: {player.coins}                  
    Realm: {player.current_realm} | Round: {current_round}                                           

""" + Style.RESET_ALL
)