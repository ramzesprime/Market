import sqlite3

# 1
conn = sqlite3.connect("store.db")
cursor = conn.cursor()

cursor.executescript("""
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price INTEGER NOT NULL
);

INSERT INTO items (name, price) VALUES 
('apple', 100),
('tomato', 200),
('Coke', 170),
('Cheese', 232),
('Wine', 500);
""")

conn.commit()
conn.close()

print("First databse created")

conn2 = sqlite3.connect("stats.db")
cursor2 = conn2.cursor()

cursor2.executescript("""
CREATE TABLE IF NOT EXISTS stats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    amount INT NOT NULL
);

INSERT INTO stats (name, amount) VALUES 
('apple', 0),
('tomato', 0),
('Coke', 0),
('Cheese', 0),
('Wine', 0);
""")

conn2.commit()
conn2.close()

print("Second database created")
