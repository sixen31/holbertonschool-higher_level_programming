#!/usr/bin/python3
"""MyList Class that inherits from List
"""


class Base:
    """
    Base class for managing ID attribute in all future classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base object.

        Args:
            id (int, optional): The ID for the object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def get_nb_objects(cls):
        return cls.__nb_objects
