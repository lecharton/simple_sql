import sqlite3


class SpaceShip:

    ship_types = {
        'F': 'Frigate',
        'R': 'Racing ship'
    }

    def __init__(self, name, ship_class, ship_type):
        self.name = name
        self.ship_class = ship_class
        self.ship_type = ship_type

    def __str__(self):
        return self.name

    def info(self):
        return {
            'Name': self.name,
            'Ship Class': self.ship_class,
            'Ship Type': self.ship_types[self.ship_type]
        }

SPACESHIPS = """
    SELECT * FROM spaceships ORDER BY name
"""

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

data_space_ships = [row for row in cursor.execute(SPACESHIPS)]

conn.close()

for data in data_space_ships:
    ship = SpaceShip(*data)
    print(ship)
    print(ship.info())
