#!/usr/bin/python3
"""
Affiche tous les états d'une base de données MySQL en fonctio
n d'un nom d'état donné en entrée,
en évitant les injections SQL.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=password,
        db=db_name,
        port=3306
    )

    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (state_name,)
    )

    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db.close()
