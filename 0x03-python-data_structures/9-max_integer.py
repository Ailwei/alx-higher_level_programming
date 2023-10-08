#!/usr/bin/python3
def max_integer(my_list=[]):
    # Check if the list is empty
    if not my_list:
        return None

    # Initialize max_value with the first element of the list
    max_value = my_list[0]

    # Initialize index to 1 to start comparing from the second element
    index = 1

    # Get the length of the list
    length = len(my_list)

    # Use a while loop to iterate through the list
    while index < length:
        current_value = my_list[index]
        if current_value > max_value:
            max_value = current_value
        index += 1

    return max_value
