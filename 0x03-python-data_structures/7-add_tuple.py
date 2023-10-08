#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure each tuple has at least 2 elements, or use 0 for missing elements
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    
    result = tuple(x + y for x, y in zip(a, b))
    
    return result
