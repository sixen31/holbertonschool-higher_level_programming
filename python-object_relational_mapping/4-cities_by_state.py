#!/usr/bin/python3
"""
Affiche toutes les villes de la base de données hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=password,
        db=db_name,
        port=3306
    )

    cur = db.cursor()

    cur.execute(
        """SELECT cities.id, cities.name, states.name FROM cities JOIN
        states ON cities.state_id = states.id ORDER BY cities.id ASC"""
    )

    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db.close()
