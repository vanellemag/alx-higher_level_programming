#!/usr/bin/python3
"""
selct_states
"""
import sys
import MySQLdb
import psycopg
"""import re"""
if __name__ == '__main__':
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]
    e = sys.argv[4]
    db = psycopg.connect(host="localhost", port=3306, user=u, passwd=p, db=d)
    cur = db.cursor()
    cur.execute(f"SELECT * FROM states WHERE name=%(username)s;",{'username': e})
    for row in cur.fetchall:
        print(row)
