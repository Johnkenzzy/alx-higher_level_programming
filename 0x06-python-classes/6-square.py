#!/usr/bin/python3
"""This module contains a class square (based on 5-square.py)
"""


class Square:
    """A shape with 4 equal sides."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with a given size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieves the size of a square object

        Returns:
            int: The size of the class instance
        """

        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the square size of a class instance.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the quare.

        Returns:
            tuple: The position of the class instance
        """

        return (self.__position)

    @position.setter
    def position(self, value):
        """Sets the position of the aquare."""

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2 or (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the # times the size of the square."""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                if self.__position[0] == 0:
                    print('#' * self.__size)
                else:
                    print(' ' * (self.__position[0] - 1), '#' * self.__size)
