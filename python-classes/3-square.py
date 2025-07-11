#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """Class that defines a square by its size."""

    def __init__(self, size=0):
        self.size = size  # setter üzerinden kontrol edilecek

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
