#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    lg = (len(sys.argv) - 1)

    if lg == 1:
        print("1 argument:")
    elif lg == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(lg))

    for x in range(1, len(sys.argv)):
        print("{:d}:".format(x), str(sys.argv[x]))
