CREATE TABLE items (
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
