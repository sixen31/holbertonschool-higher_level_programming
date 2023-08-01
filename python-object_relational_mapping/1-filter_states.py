#!/usr/bin/python3
# List all states with a name starting with uppercase N
# Username, password, and database names are given as user args

import MySQLdb
import sys

if __name__ == "__main__":
    user_db = sys.argv[1]
    passwd_db = sys.argv[2]
    name_db = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost", user=user_db, passwd=passwd_db, db=name_db, port=3306
            )

    cursor = db.cursor()

    cursor.execute(
            """
        SELECT * FROM states
        WHERE BINARY name
        LIKE 'N%'
        ORDER BY states.id ASC
        """
        )

    results = cursor.fetchall()

    for element in results:
        print(element)

    db.close()
