#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = list()

    for i in range(len((my_list_1))):
        try:
            result = my_list_1[i] / my_list_2[i]

        except ZeroDivisionError:
            result = 0
            print("division by 0")

        except TypeError:

            result = 0
            print("wrong type")

        except IndexError:

            result = 0
            print("out of range")


        finally:
            newlist.append(result)

    return(newlist)
