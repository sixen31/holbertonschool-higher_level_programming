#!/usr/bin/python3
"""
Module pour récupérer tous les objets State contenant la lettre "a"
de la base de données hbtn_0e_6_usa
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

    """Création d'une session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Récupération de tous les objets State contenant la lettre "a" """
    states = session.query(State).filter
    (State.name.like('%a%')).order_by(State.id)

    """Affichage des résultats"""
    for state in states:
        print("{}: {}".format(state.id, state.name))
