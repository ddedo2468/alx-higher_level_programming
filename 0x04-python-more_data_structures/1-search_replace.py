#!/usr/bin/python3
def search_replace(my_list, search, replace):

    newlist = []
    for element in my_list:
        if element == search:
            newlist.append(replace)
        else:
            newlist.append(element)
    return newlist

