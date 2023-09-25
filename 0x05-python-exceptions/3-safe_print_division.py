#!/usr/bin/python3
def safe_print_division(a, b):
   """divide 2 numbers safly"""
    try:
        result = a/b

    except:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
