#!/usr/bin/python3

import sys

if __name__ == "__main__":

    num_args = len(isys.argv) -1

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} argument:".format(num_args))

        for i in range(1, num_args + 1):
            print("{:d}: {}".format(i, sys.argv[i]))
