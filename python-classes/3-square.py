#!/usr/bin/python3
'''definie classe'''


class Square:
    """Cette classe définit un carré."""

    def __init__(self, size=0):
        """Initialise une instance de la classe Square.

        Args:
            size (int): La taille du carré. Valeur par défaut est 0.

        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est inférieur à 0.
        """
        if not isinstance(size, int):
            raise TypeError("size doit être un entier")
        if size < 0:
            raise ValueError("size doit être >= 0")
        self.__size = size

    def area(self):
        """Calcule l'aire du carré.

        Returns:
            int: L'aire du carré.
        """
        return self.__size ** 2
