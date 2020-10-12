import csv
import sqlite3

# connect to a sqlite3 database in memory & create tables
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE videogames(platform TEXT, name TEXT PRIMARY KEY, publisher TEXT)")

# begin read psp csv file into dictionary & insert into matching table
with open('psp.csv', 'r') as fin:
    dr = csv.reader(fin)
    to_db = []
    for line in dr:
        to_db.append(line)

cur.executemany("INSERT INTO videogames(platform, name, publisher) VALUES(?, ?, ?)", to_db)
con.commit()

# begin read ds csv file into dictionary & insert into matching table
with open('ds.csv', 'r') as fin:
    dr = csv.reader(fin)
    to_db = []
    for line in dr:
        to_db.append(line)

cur.executemany("INSERT INTO videogames(platform, name, publisher) VALUES(?, ?, ?)", to_db)
con.commit()

# begin read ps3 csv file into dictionary & insert into matching table
with open('ps3.csv', 'r') as fin:
    dr = csv.reader(fin)
    to_db = []
    for line in dr:
        to_db.append(line)

cur.executemany("INSERT INTO videogames(platform, name, publisher) VALUES(?, ?, ?)", to_db)
con.commit()

# begin read switch csv file into dictionary & insert into matching table
with open('switch.csv', 'r') as fin:
    dr = csv.reader(fin)
    to_db = []
    for line in dr:
        to_db.append(line)

cur.executemany("INSERT INTO videogames(platform, name, publisher) VALUES(?, ?, ?)", to_db)
con.commit()

# begin read 3ds csv file into dictionary & insert into matching table
with open('3ds.csv', 'r') as fin:
    dr = csv.reader(fin)
    to_db = []
    for line in dr:
        to_db.append(line)

cur.executemany("INSERT INTO videogames(platform, name, publisher) VALUES(?, ?, ?)", to_db)
con.commit()

# begin read gba csv file into dictionary & insert into matching table
with open('gba.csv', 'r') as fin:
    dr = csv.reader(fin)
    to_db = []
    for line in dr:
        to_db.append(line)

cur.executemany("INSERT INTO videogames(platform, name, publisher) VALUES(?, ?, ?)", to_db)
con.commit()

# begin user input
print("\n")
prompt = "\nWhat console would you like to see? "
message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        cur.execute("SELECT * FROM videogames WHERE platform='{}'".format(message))
        rows = cur.fetchall()
        for row in rows:
            print(row) 

# close the connection to the sqlite3 database in memory
con.close()
