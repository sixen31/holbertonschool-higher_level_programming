#!/usr/bin/python3
"""
Module pour afficher tous les objets City de la base
 de données hbtn_0e_14_usa triés par ordre croissant d'id
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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

    """Recherche de tous les objets City triés par ordre croissant d'id"""
    cities = session.query(City).order_by(City.id).all()

    """Affichage des résultats"""
    for city in cities:
        state_name = session.query(State.name).filter
        (State.id == city.state_id).first()[0]
        print("{}: ({}) {}".format(state_name, city.id, city.name))
