import sqlite3

class DatabaseManager:
    def __init__(self, db_name="game_booty.db"):
        self.db_name = db_name
        self.setup_database()

    def setup_database(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            player_name TEXT NOT NULL,
            item_name TEXT NOT NULL,
            quantity INTEGER,
            PRIMARY KEY(player_name, item_name)
        )
        """)

        conn.commit()
        conn.close()

    def load_inventory(self, player_name):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("SELECT item_name, quantity FROM inventory WHERE player_name=?", (player_name,))

        items = cursor.fetchall()
        conn.close()

        return {item: quantity for item, quantity in items}

    def save_inventory(self, player_name, inventory):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        #clears current items for the player to avoid duplicates
        cursor.execute("DELETE FROM inventory WHERE player_name=?", (player_name,))

        for item, quantity in inventory.items():
            cursor.execute("INSERT INTO inventory (player_name, item_name, quantity) VALUSE (?,?,?)", (player_name, item, quantity))

        conn.commit()
        conn.close()