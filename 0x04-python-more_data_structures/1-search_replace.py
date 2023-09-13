#!/usr/bin/python3
def search(my_list, search, replace):
    newlist = list()
    for element in my_list:
        if element == search:
            newlist.append(replace)
        else:
            newlist.append(element)
    return newlist

