import sqlite3

ADD_ROCINANTE = """
INSERT INTO spaceships
VALUES ("Rocinante", "Corvette", "F")
"""


conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute(ADD_ROCINANTE)

conn.commit()
conn.close()