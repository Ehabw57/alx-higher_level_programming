#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lenth = len(argv)
    if lenth < 1:
        print("0")
    else:
        r = 0
        for i in range(1, lenth):
            r += int(argv[i])
        print("{}".format(r))
