#!/usr/bin/python3
""" Define Class Rectangle """


class Rectangle:
    """Defines A Rectangle"""
    def __init__(self, width=0, height=0):
        """ construction function """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the Rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ get the rectangle height """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ calculating rectangle area """
        return self.__width * self.height

    def perimeter(self):
        """ calculate rectangle primeter """
        if self.__width == 0 or self.height == 0:
            return 0
        else:
            return (self.__width + self.height) * 2

    def __str__(self):
        """ refactor str for rectangle class """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """ more readable string """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ mesaage when obj is deleted """
        print("Bye rectangle...")
