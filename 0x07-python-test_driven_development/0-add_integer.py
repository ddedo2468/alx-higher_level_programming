#!/usr/bin/python3
"""
This is the "Add Integer"  module.
"""


def add_integer(a, b):
    """Return the sum of two integers or floats as an integer."""
    mapp = list(map(lambda ent: isinstance(ent, (int, float)), [a, b]))

    if all(mapp):
        return int(a) + int(b)

    for x, y in list(zip(mapp, ['a', 'b'])):
        if not x:
            raise TypeError("{} must be an integer".format(y))
