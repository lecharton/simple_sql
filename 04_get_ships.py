import sqlite3


SPACESHIPS = """
    SELECT * FROM spaceships ORDER BY name
"""

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

for row in cursor.execute(SPACESHIPS):
    print(row)

conn.close()