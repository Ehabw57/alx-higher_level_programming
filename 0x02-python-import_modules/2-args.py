#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lenth = len(argv) - 1
    if lenth != 1:
        if lenth == -1:
            print("{} arguments.".format(lenth))
        else:
            print("{} arguments:".format(lenth))
    else:
        print("{} argument:".format(lenth))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
