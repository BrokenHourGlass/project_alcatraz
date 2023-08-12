from databaseManager import DatabaseManager

class Player:
    def __init__(self, name, location="Starting Area"):
        self.name = name
        self.location = location
        
        # Initialize stats with some default values. 
        # You can modify this or make it more dynamic as needed.
        self.stats = {
            "str": 10,
            "dex": 10,
            "con": 10,
            "int": 10,
            "wis": 10,
            "cha": 10
        }

        self.db_manager = DatabaseManager("game_db.db")
        self.inventory = self.db_manager.load_inventory(self.name)

    def update_location(self, new_location):
        self.location = new_location

    def update_stat(self, stat, value):
        if stat in self.stats:
            self.stats[stat] = value

    def add_to_inventory(self, item, quantity=1):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity
        self.db_manager.save_inventory(self.name, self.inventory)

    def remove_from_inventory(self, item, quantity=1):
        if item in self.inventory:
            self.inventory[item] -= quantity
            if self.inventory[item] <= 0:
                del self.inventory[item]
        self.db_manager.save_inventory(self.name, self.inventory)

    def get_stat(self, stat):
        return self.stats.get(stat)

    def get_inventory(self):
        return self.inventory
