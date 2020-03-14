# Let's test with python and SQlite
# written by plscks
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

c.execute("INSERT INTO all_data (province, country, last_updated, confirmed, deaths, recovered) VALUES ('Washington', 'US', 'today', 3000, 900, 20)")

conn.commit()
conn.close()
