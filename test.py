import sqlite3

connection = sqlite3.connect('database/ray.db')
cursor = connection.cursor()

query = "Select * from users"
cursor.execute(query)
data = cursor.fetchall()
print(data)