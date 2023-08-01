#!/usr/bin/python3

"""lists all states, filtered by user input, database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    user_db = sys.argv[1]
    passwd_db = sys.argv[2]
    name_db = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=user_db,
        passwd=passwd_db,
        db=name_db,
        port=3306
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cursor.execute(query, (state_name,))

    results = cursor.fetchall()

    for element in results:
        print(element)

    db.close()
