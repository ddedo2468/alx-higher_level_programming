#!/usr/bin/python3
"""Class Square Define"""


class Square:
    """ this is a class that presents a square"""
    def __init__(self, size):
        """ this is the contructor of the class
        it has 1 arg size"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
