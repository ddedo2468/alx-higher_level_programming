#!/usr/bin/python3
"""
myList Module documentatiom
"""


class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """class constructor the object"""
        super().__init__()

    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
