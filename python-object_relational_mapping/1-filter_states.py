#!/usr/bin/python3



import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Utilisation : {} <nom_utilisateur> <mot_de_passe> <nom_base_de_donnees>".format(sys.argv[0]))
        sys.exit(1)

    user = sys.argv[1]
    pasd = sys.argv[2]
    data = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=pasd, db=data

    curseur = db.cursor()

    curseur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    resultats = curseur.fetchall()
    for ligne in resultats:
        print(ligne)

    curseur.close()
    db.close()
