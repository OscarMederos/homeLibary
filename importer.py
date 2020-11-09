import csv
import sqlite3

# connect to a sqlite3 database in memory & create tables
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE videogames(platform TEXT, name TEXT PRIMARY KEY, publisher TEXT)")

# begin read csv file into a list & insert into table
with open('switch.csv', 'r') as fin:
    dr = csv.reader(fin)
    to_db = []
    for line in dr:
        to_db.append(line)

cur.executemany("INSERT INTO videogames(platform, name, publisher) VALUES(?, ?, ?)", to_db)
con.commit()

# output the contents of a table to verify integrity
cur.execute("SELECT platform, name, publisher FROM videogames")
rows = cur.fetchall()
for row in rows:
    print(row)

# close the connection to the sqlite3 database in memory
con.close()