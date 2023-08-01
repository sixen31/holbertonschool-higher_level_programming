#!/usr/bin/python3


import MySQLdb
import sys

if __name__ == "__main__":

    user = sys.argv[1]
    pasd = sys.argv[2]
    data = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost", port=3306, user=user, passwd=pasd, db=data)

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    results = cur.fetchall()
    for row in results:
        print(row)

    cur.close()
    db.close()
