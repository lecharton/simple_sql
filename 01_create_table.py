import sqlite3

CREATE_TABLE = """
CREATE TABLE "spaceships" (
    "name" varchar(128) NOT NULL,
    "ship_class" varchar(128) NOT NULL,
    "type" varchar(1) NOT NULL
);
"""


conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute(CREATE_TABLE)

conn.commit()
conn.close()