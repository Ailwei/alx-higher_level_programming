#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []  # Initialize an empty list to store the True/False values
    for num in my_list:
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
