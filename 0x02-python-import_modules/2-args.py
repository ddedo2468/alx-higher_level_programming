#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    ArgCount = len(sys.argv) - 1
    if ArgCount == 0:
        print("0 arguments.")
    elif ArgCount == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(ArgCount))
    for i in range(ArgCount):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
