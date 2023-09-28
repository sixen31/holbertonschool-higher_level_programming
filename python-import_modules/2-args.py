#!/usr/bin/python3

import sys

if __name__ == '__main__':
    args = sys.argv[1:]
    num_args = len(args)

    if num_args == 0:
        print("{} arguments.".format(num_args))
    else:
        print("{} argument{}:".format(num_args, "" if num_args == 1 else "s"))
        for i, arg in enumerate(args, 1):
            print("{}: {}".format(i, arg))
