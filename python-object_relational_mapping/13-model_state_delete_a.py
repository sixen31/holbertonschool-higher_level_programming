#!/usr/bin/python3
"""
Module pour supprimer tous les objets State contenant
la lettre "a" dans leur nomde la base de données hbtn_0e_6_usa
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

    """Recherche des objets State contenant la lettre "a" dans leur nom"""
    states = session.query(State).filter(State.name.like('%a%')).all()

    """Suppression des objets State trouvés"""
    for state in states:
        session.delete(state)
    session.commit()
