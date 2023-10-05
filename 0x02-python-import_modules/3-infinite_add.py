#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # Exclude the script name from the list of arguments

    # Initialize a variable to store the sum
    total = 0

    # Iterate through the arguments, cast them to integers, and add to the total
    for arg in argv:
        total += int(arg)

    # Print the total sum after processing all arguments
    print(total)
