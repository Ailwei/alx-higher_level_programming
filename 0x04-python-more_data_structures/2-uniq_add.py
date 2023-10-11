#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_numbers = set()
    total = 0
    
    for i in my_list:
        if i not in unique_numbers:
           unique_numbers.add(i)
           total += i
    return total        
