#!/usr/bin/python3
"""
Ajouter l'objet State "Louisiana" à la base de données hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """Vérification du nombre d'arguments"""
    if len(sys.argv) != 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        sys.exit(1)

    """Connexion à la base de données MySQL"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    """Création d'une session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """Création de l'objet State "Louisiana" """
    new_state = State(name='Louisiana')

    """Ajout de l'objet State à la base de données"""
    session.add(new_state)
    session.commit()

    """Affichage de l'id de l'objet State créé"""
    print(new_state.id)
