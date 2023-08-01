#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Utilisation : {} <nom_utilisateur> <mot_de_passe> <nom_base_de_donnees>".format(sys.argv[0]))
        sys.exit(1)

    nom_utilisateur = sys.argv[1]
    mot_de_passe = sys.argv[2]
    nom_base_de_donnees = sys.argv[3]

    try:
        # Connectez-vous à la base de données MySQL
        db = MySQLdb.connect(host="localhost", port=3306, user=nom_utilisateur, passwd=mot_de_passe, db=nom_base_de_donnees)

        curseur = db.cursor()

        curseur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

        resultats = curseur.fetchall()
        for ligne in resultats:
            print(ligne)

        curseur.close()
        db.close()

    except MySQLdb.Error as e:
        print("Erreur lors de la connexion à la base de données MySQL : {}".format(e))
        sys.exit(1)
