#!/usr/bin/python3
#!/usr/bin/python3

"""
This module contains a function that prints a square using the '#' character.
"""

def print_square(size):
    """
    This function prints a square of '#' characters of the given size.

    Args:
        size (int): The size of the square to be printed.

    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is less than 0.

    Returns:
        None.
    """
    # Check if `size` is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    # Check if `size` is greater than or equal to 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for i in range(size):
        print('#' * size)
