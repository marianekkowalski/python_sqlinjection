#!/usr/bin/env python3
import sqlite3
import sys

for arg in sys.argv:
    print("ARG: %s" % arg)

con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE apius(id INTEGER PRIMARY KEY, name VARCHAR UNIQUE)")

q = "INSERT INTO apius(name) VALUES('%s')"

with con:
    print("Trying to insert into database")
    con.execute(q % ("s%ss" % sys.argv[1]))
    con.execute("INSERT INTO apius(name) VALUES(?)", ("Python",))
    print("Pushing args[1]...")
    call_list = [lambda x: x.execute(q % sys.argv[1])]
    call_list[0](con)

cur = con.execute("SELECT * FROM apius")
print(cur.fetchall())

con.close()
