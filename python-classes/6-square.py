#!/usr/bin/python3
'''executable'''


class Square:
    """Cette classe définit un carré."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise une instance de la classe Square.

        Args:
            size (int): La taille du carré. Valeur par défaut est 0.
            position (tuple): La position du carré. Valeur par défaut est (0, 0).

        Raises:
            TypeError: Si size n'est pas un entier ou si position n'est pas un tuple de deux entiers positifs.
            ValueError: Si size est inférieur à 0 ou si l'un des éléments de position est inférieur à 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Récupère la position du carré."""
        return self.__position

    @position.setter
    def position(self, value):
        """Définit la position du carré.

        Args:
            value (tuple): La nouvelle position du carré.

        Raises:
            TypeError: Si value n'est pas un tuple de deux entiers positifs.
            ValueError: Si l'un des éléments de value est inférieur à 0.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) for i in value) or \
                not all(i >= 0 for i in value):
            raise TypeError("position doit être un tuple de deux entiers positifs")
        self.__position = value

    def area(self):
        """Calcule l'aire du carré.

        Returns:
            int: L'aire du carré.
        """
        return self.__size ** 2

    def my_print(self):
        """Affiche le carré avec le caractère # en utilisant la position."""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
