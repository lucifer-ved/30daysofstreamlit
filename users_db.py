import sqlite3

# Connect to the database (creates it if not exists)
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create table for users
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

# Insert sample users
users = [
    ('admin', 'admin_password'),
    ('user', 'user_password')
]

# Insert sample data into the users table
c.executemany('INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)', users)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully, and users inserted.")