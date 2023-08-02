#!/usr/bin/python3
"""
Module pour récupérer l'objet State correspondant au nom passé en argument
de la base de données hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """Vérification du nombre d'arguments"""
    if len(sys.argv) != 5:
        print("Usage: {} username password database_name state_name"
              .format(sys.argv[0]))
        sys.exit(1)

    """Connexion à la base de données MySQL"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    """Création d'une session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """Récupération de l'objet State correspondant au nom passé en argument"""
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    """Affichage du résultat ou de "Not found" si l'objet n'existe pas"""
    if state is None:
        print("Not found")
    else:
        print(state.id)
