import sqlite3

# Connect to the database
connection = sqlite3.connect("students.db")

# Create a cursor
cursor = connection.cursor()

# Execute PRAGMA query
cursor.execute("PRAGMA table_info(students);")

# Get all rows
columns = cursor.fetchall()

# Print each row
for column in columns:
    print(column)

# Close connection
connection.close()