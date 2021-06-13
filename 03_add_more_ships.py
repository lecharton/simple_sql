import sqlite3


MORE = [
    ("Razorback", "Proserpina Starworks Series 6 Sunflare Racing Pinnace", "R"),
    ("Anubis", "Amun-Ra-class stealth frigate", "F")
]

INSERT_MORE = """
INSERT INTO spaceships VALUES (?, ?, ?)
"""

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.executemany(INSERT_MORE, MORE)

conn.commit()
conn.close()