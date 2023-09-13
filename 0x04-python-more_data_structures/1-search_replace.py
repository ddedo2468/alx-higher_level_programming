#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    a function that search for enelmint in array and change it
    with another element parameter
    """

    newlist = []
    for element in my_list:
        if element == search:
            newlist.append(replace)
        else:
            newlist.append(element)
    return newlist
