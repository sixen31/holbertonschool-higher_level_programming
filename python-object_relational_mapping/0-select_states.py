#!/usr/bin/python3


import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

        cur = db.cursor()

        cur.execute("SELECT * FROM states ORDER BY id ASC")

        results = cur.fetchall()
        for row in results:
            print(row)

        cur.close()
        db.close()
