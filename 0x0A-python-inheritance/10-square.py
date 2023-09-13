#!/usr/bin/python3
"""A class Square that inherits from Rectangle (9-rectangle.py):"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Statemnet of the square class."""

    def __init__(self, size):
        """Initializes the size.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
