# Run the program
- python main.py

# Game Rules

Win -->  player reach level 100
Loss --> health point = 0

[i] Player will play the 10x10 board game
[ii] He will start with level 0(starting point), HP=10, coins=0 
[iii] Need to play 5 rounds (1 round = 20 cells) -> 1 cell equal to 1 level
[iv] Each cell has its own magic
[v] There will be 5 Themes (Ice realm, Fire Realm, Shadow Realm, Space Realm, Void Realm) -> Each Realm has its magic theme
[vi] Player will start from Ice Realm, and he can choose what realm he wants to be in next round. But, cannot choose same realm twice(except Realm cell)


# Realm Rules

# Ice Realm
- Frost Attack: First enemy attack in this realm deals +2 damage.
- Frozen Trap: Trap cells only reduce levels, not HP.

# Fire Realm
- Flame Surge: Every enemy defeated gives +1 level bonus.
- Burning Coin: Coin cards give +7 coins instead of +5.

# Shadow Realm
- Shadow Trap: Defense cards not working on any enemy of rank 
- Dark Bargain: Mystery cells always trigger (no skip). 

# Space Realm
- Warp Step: Portal dice rolls always move forward (never backward).
- Cosmic Leap: Time magic in shop gives +7 levels instead of +5.

# Void Realm
- Void Immunity: Immune magic can be used twice in this realm.
- Abyssal Trap: Trap cells deal both HP and level loss (-3 HP, -3 levels).

# Cell magic

Card cell:
	Player need to pick one of 3 cards:
	(i) Health card = +5 hp
	(ii) Defense card = can defense enemy 
	(ii) Coin card = +5 coin

-- 1 defense card can defense elite rank enemies
-- 2 defense cards can defense master rank enemies
-- 3 defense cards can defense epic rank enemies

Enemy cell:
	player will be randomly attacked by one of monsters 
	Elite Rank: 
		(i) Zombie = -3 hp
		(ii) Werewolf = -2 hp and -1 level
	Master rank:
		(i) Vampire = -4 hp
		(ii) Demon = -3 hp and -1 levels
	Epic Rank:
		(i) Dragon = -5 hp
		(ii) Beast = -4 hp and -1 level


Trap cell:
	player will lose -5 hp or -5 levels randomly 

Mystery cell:
	player will get bad or good luck randomly
	bad luck = -5 hp and -2 levels
	good luck = +5 coins and + 3 levels

Shop cell:	
	Player can buy items in shop with his coins:
	(i) Health magic = +5 hp
	(ii) Tank magic = can defense any enemy of rank
	(iii) Time magic = can move +5 levels
	(iv) Immune magic = can skip any cell the player once
	(v) Gold magic = +5 coins


Portal cell:
	If a player get to this cell, two dice will be rolled, 
	first dice --> odd number= backward or even number=forward
	second dice --> steps

Realm cell:
	A player can choose the any realm he want for next round (can be same realm)

Treasure cell:
	Player need to choose one of 3 items:
	(i) Gemstone = +6 coins
	(ii) Ancient scroll = +2 defense cards
	(iii) Mystic portion = +3 hp and +1 level

Cursed cell:
	need to choose one of 2 items:
	(i) Weakness curse = -2 defense cards
	(ii) Decay curse = -3 hp and -2 coins

Altar cell:
	need to choose one of 3 items:
	Sacrifice Coins = Lose 5 coins, gain +2 defense cards
	Sacrifice HP = Lose 3 hp, gain +5 levels
	Sacrifice Levels = Lose 2 levels, gain +5 coins
