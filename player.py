class Player:
    def __init__(self, name, health=100, coin=0, level=1, realm="Mortal World"):
        # Temporary data held in memory
        self.name = name
        self.health = health
        self.coin = coin
        self.level = level
        self.realm = realm

    def show_status(self):
        """Display current temporary stats."""
        print(f"\n--- {self.name}'s Stats ---")
        print(f"Health: {self.health} | Coins: {self.coin}")
        print(f"Level: {self.level} | Realm: {self.realm}")
        print("--------------------------")
