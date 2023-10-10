#!/usr/bin/python3
'''executable'''


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
        self.__size = size

    @property
    def size(self):
        """Récupère la taille du carré."""
        return self.__size

    @size.setter
    def size(self, value):
        """Définit la taille du carré.

        Args:
            value (int): La nouvelle taille du carré.

        Raises:
            TypeError: Si value n'est pas un entier.
            ValueError: Si value est inférieur à 0.
        """
        if not isinstance(value, int):
            raise TypeError("size doit être un entier")
        if value < 0:
            raise ValueError("size doit être >= 0")
        self.__size = value

    def area(self):
        """Calcule l'aire du carré.

        Returns:
            int: L'aire du carré.
        """
        return self.__size ** 2

    def my_print(self):
        """Affiche le carré avec le caractère #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
