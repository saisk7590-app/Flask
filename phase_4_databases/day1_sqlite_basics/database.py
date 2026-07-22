import sqlite3

# Connect to the database
connection = sqlite3.connect("students.db")

# Create a cursor object
cursor = connection.cursor()

# Open and read the SQL file
with open("schema.sql", "r") as file:
    sql_script = file.read()

# Execute the SQL script
cursor.executescript(sql_script)

# Save the changes
connection.commit()

# Close the connection
connection.close()

print("Database and table created successfully!")