#!/usr/bin/python3
"""
Affiche toutes les donné de la base de données hbtn_0e_4_usa.
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
        """SELECT cities.name FROM cities JOIN
        states ON cities.state_id = states.id WHERE 
        states.name=%s ORDER BY cities.id ASC""",
        (state_name,)
    )

    results = cur.fetchall()

    cities = ", ".join([row[0] for row in results])

    print(cities)

    cur.close()
    db.close()
