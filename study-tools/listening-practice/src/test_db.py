import sqlite3

# Connect to the database
conn = sqlite3.connect('listening_practice.db')
cursor = conn.cursor()

# Check videos table
cursor.execute("SELECT * FROM videos")
print("Videos in database:", cursor.fetchall())

# Check transcripts table
cursor.execute("SELECT COUNT(*) FROM transcripts")
print("Number of transcript entries:", cursor.fetchall()[0][0])

conn.close()