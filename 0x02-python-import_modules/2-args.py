#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    print("{:d} {:s}{:c}".format(length - 1, "argument" if length < 2 else "arguments",
    "." if length == 1 else ":"))
    for i, string in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, string))