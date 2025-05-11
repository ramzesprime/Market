import sqlite3

conn = sqlite3.connect("database.db")  # Подключение к файлу базы данных
cursor = conn.cursor()

with open("queries.sql", "r") as sql_file:
    sql_script = sql_file.read()
    cursor.executescript(sql_script)  # Выполнение команд из файла

conn.commit()
conn.close()

print("SQL script executed successfully!")
