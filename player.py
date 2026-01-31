class Player:
    def __init__(self):
        self.health = 10
        self.level = 0
        self.coins = 0
        self.is_alive = True
        self.defense_cards = 0
        self.inventory = {
            "Tank magic": 0,
            "Immune magic": 0,
        }
        self.next_realm = None
        self.current_realm = "Ice Realm"
        self.realm_used = ["Ice Realm"]
        self.position = 0

    def change_level(self, steps):
        new_level = self.level + steps
        if new_level > 100:
            new_level = 100
        self.level = new_level

    def change_position(self, steps):
        self.position += steps

    def change_health(self, amount):
        self.health += amount
        if self.health < 0:
            self.health = 0
            self.is_alive = False

    def change_coins(self, amount):
        self.coins += amount
        if self.coins < 0:
            self.coins = 0

    def add_defense_cards(self, amount):
        self.defense_cards += amount
        if self.defense_cards < 0:
            self.defense_cards = 0

    def set_level(self, level_start):
        self.level = level_start

        