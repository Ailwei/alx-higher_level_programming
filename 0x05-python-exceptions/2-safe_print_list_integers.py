#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0  # To keep track of the number of integers printed
    try:
        for item in my_list:
            if isinstance(item, int):
                print("{:d}".format(item), end="")
                count += 1

            if count == x:
                break  # Stop when x integers have been printed
        print()
        return count
    except TypeError:
        return count
