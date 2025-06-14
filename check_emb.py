import sqlite3

conn = sqlite3.connect("knowledge_base.db")
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM discourse_chunks WHERE embedding IS NOT NULL")
print("Embedded chunks:", cursor.fetchone()[0])
conn.close()
