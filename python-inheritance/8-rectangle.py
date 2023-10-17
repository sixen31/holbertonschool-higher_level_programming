#!/usr/bin/python3
"""define python"""
Rectangle = __import__('8-rectangle').Rectangle


class Basegeometry:
    """Define class"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area"""
        return self.width * self.height
