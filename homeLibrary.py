import csv
import sqlite3

# connect to a sqlite3 database in memory & create tables
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE psp(name TEXT PRIMARY KEY, publisher TEXT)")
cur.execute("CREATE TABLE ds(name TEXT PRIMARY KEY, publisher TEXT)")
cur.execute("CREATE TABLE ps3(name TEXT PRIMARY KEY, publisher TEXT)")
cur.execute("CREATE TABLE switch(name TEXT PRIMARY KEY, publisher TEXT)")
cur.execute("CREATE TABLE \"3ds\"(name TEXT PRIMARY KEY, publisher TEXT)")
cur.execute("CREATE TABLE gba(name TEXT PRIMARY KEY, publisher TEXT)")
cur.execute("CREATE TABLE ps4(name TEXT PRIMARY KEY, publisher TEXT)")
cur.execute("CREATE TABLE wii(name TEXT PRIMARY KEY, publisher TEXT)")
cur.execute("CREATE TABLE xboxone(name TEXT PRIMARY KEY, publisher TEXT)")
cur.execute("CREATE TABLE ps1(name TEXT PRIMARY KEY, publisher TEXT)")
cur.execute("CREATE TABLE xbox360(name TEXT PRIMARY KEY, publisher TEXT)")
cur.execute("CREATE TABLE xbox(name TEXT PRIMARY KEY, publisher TEXT)")
cur.execute("CREATE TABLE wiiu(name TEXT PRIMARY KEY, publisher TEXT)")


# begin read psp csv file into dictionary & insert into matching table
with open('psp.csv', 'r') as fin:
    dr = csv.reader(fin)
    to_db = []
    for line in dr:
        to_db.append(line)

cur.executemany("INSERT INTO psp(name, publisher) VALUES(?, ?)", to_db)
con.commit()

# begin read ds csv file into dictionary & insert into matching table
with open('ds.csv', 'r') as fin:
    dr = csv.reader(fin)
    to_db = []
    for line in dr:
        to_db.append(line)

cur.executemany("INSERT INTO ds(name, publisher) VALUES(?, ?)", to_db)
con.commit()

# begin read ps3 csv file into dictionary & insert into matching table
with open('ps3.csv', 'r') as fin:
    dr = csv.reader(fin)
    to_db = []
    for line in dr:
        to_db.append(line)

cur.executemany("INSERT INTO ps3(name, publisher) VALUES(?, ?)", to_db)
con.commit()

# begin read switch csv file into dictionary & insert into matching table
with open('switch.csv', 'r') as fin:
    dr = csv.reader(fin)
    to_db = []
    for line in dr:
        to_db.append(line)

cur.executemany("INSERT INTO switch(name, publisher) VALUES(?, ?)", to_db)
con.commit()

# begin read 3ds csv file into dictionary & insert into matching table
with open('3ds.csv', 'r') as fin:
    dr = csv.reader(fin)
    to_db = []
    for line in dr:
        to_db.append(line)

cur.executemany("INSERT INTO \"3ds\"(name, publisher) VALUES(?, ?)", to_db)
con.commit()

# begin read gba csv file into dictionary & insert into matching table
with open('gba.csv', 'r') as fin:
    dr = csv.reader(fin)
    to_db = []
    for line in dr:
        to_db.append(line)

cur.executemany("INSERT INTO gba(name, publisher) VALUES(?, ?)", to_db)
con.commit()

# output the contents of a table to verify integrity
cur.execute("SELECT name, publisher FROM gba")
rows = cur.fetchall()
for row in rows:
    print(row)

con.close()
