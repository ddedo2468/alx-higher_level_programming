#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argCount = len(sys.argv)
    if argCount <= 1:
        print("0 argument.")
    else:
        if argCount == 2:
            print("{:d} argument:".format(argCount - 1))
        else:
            print("{:d} arguments:".format(argCount - 1))
        for i in range(1, argCount):
            print("{:d}: {}".format(i, sys.argv[i]))
