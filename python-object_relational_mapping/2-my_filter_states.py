#!/usr/bin/python3
"""Afficher toutes les valeurs dans la table states de hbtn_0e_0_usa
où le nom correspond à l'argument donné"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute(
        """
        SELECT *
        FROM states
        WHERE states.name LIKE BINARY '{}'
        ORDER BY states.id
        """.format(sys.argv[4])
    )

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
