#!/usr/bin/python3
""" Defines a class that inherits from list"""


class MyList(list):
    """ the class definition"""
    def __init__(self):
        """ the constructor """
        super().__init__()

    def print_sorted(self):
        """ printing a sorted list """
        print sorted(self)
