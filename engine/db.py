import csv
import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect('my.db')
cursor = conn.cursor()

# # --- Create sys_command table ---
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS sys_command(
#     id INTEGER PRIMARY KEY,
#     name VARCHAR(100) UNIQUE,
#     path VARCHAR(1000)
# )
# """)

# # --- Create web_command table ---
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS web_command(
#     id INTEGER PRIMARY KEY,
#     name VARCHAR(100) UNIQUE,
#     url VARCHAR(1000)
# )
# """)

# # --- Insert web commands ---
# web_commands = [
#     ('google', 'https://www.google.com'),
#     ('youtube', 'https://www.youtube.com'),
#     ('gmail', 'https://mail.google.com'),
#     ('instagram', 'https://www.instagram.com'),
#     ('canvas', 'https://canvas.instructure.com'),  # Update if needed
#     ('facebook', 'https://www.facebook.com'),
#     ('linkedin', 'https://www.linkedin.com'),
#     ('github', 'https://www.github.com')
# ]

# cursor.executemany(
#     "INSERT OR IGNORE INTO web_command VALUES (null, ?, ?)",
#     web_commands
# )

# # --- Insert system commands (apps) ---
# sys_commands = [
#     ('wps office', 'C:\\Users\\ASUS\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\WPS Office.lnk'),
#     ('onenote', 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OneNote.lnk')
# ]

# cursor.executemany(
#     "INSERT OR IGNORE INTO sys_command VALUES (null, ?, ?)",
#     sys_commands
# )

# # Save and close
# conn.commit()
# conn.close()

# print(" Database setup complete.")
# Create a table with the desired columns
# cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')
# desired_columns_indices = [0,18]

# Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# # Commit changes and close connection
# conn.commit()
# conn.close()
# query = 'Micky'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])