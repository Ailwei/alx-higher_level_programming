#!/usr/bin/python3

class Square:
    """Represents a square with specified size and position.

    Args:
        size (int): The size of the square.
        position (tuple): The position of the square.

    Attributes:
        __size (int): A private instance attribute
        representing the size of the square.
        __position (tuple): A private instance attribute
        representing the position of the square.

    Raises:
        TypeError: If size is not an integer, or
        if position is not a tuple of two positive integers.
        ValueError: If size is less than 0.

    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square with the given size and position.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.

        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square.

        Returns:
            tuple: The position of the square as a tuple (x, y).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The new position as a tuple (x, y).

        Raises:
            TypeError: If value is not a tuple of two positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
                        raise TypeError('position must be a tuple of 2 positive integers')
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print a 2D representation of the square with '#' characters
        and '$' at the end of each line.

        If the size is 0, print an empty line.
        """

        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size, end="")
                if i < self.__size - 1:
                    print("$")
                else:
                    print()


if __name__ == "__main__":

    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--")
