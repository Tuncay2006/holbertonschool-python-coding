#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """Class that defines a square by its size."""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
