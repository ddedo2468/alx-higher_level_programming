#!/usr/bin/python3
""" Define Class Rectangle """


class Rectangle:
    """Defines A Rectangle"""
    def __init__(self, width, height):
        """ construction function """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """get the Rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
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
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
