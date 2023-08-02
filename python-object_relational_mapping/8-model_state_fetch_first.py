#!/usr/bin/python3
"""
Module pour récupérer le premier objet State de la base de données hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """Connexion à la base de données MySQL"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    """ Création d'une session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Récupération du premier objet State"""
    first_state = session.query(State).order_by(State.id).first()

    """Affichage du résultat ou de "Nothing" si la table est vide"""
    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))
