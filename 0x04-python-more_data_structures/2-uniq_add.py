#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    newList = list()

    for element in my_list:

        if element not in newList:
            newList.append(element)
            sum += element
        else:
            continue
    return sum
