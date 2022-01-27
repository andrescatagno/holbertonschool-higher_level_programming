#!/usr/bin/python3
'''
Function that returns the add of two integer numbers
'''

def add_integer(a, b=98):
    '''Function that returns the add of two integer numbers'''
    if (type (a) is float):
        a = int(a)
    if (type (b) is float):
        a = int(b)
    if(type(a) is not int):
        raise TypeError("a must be an integer")
    if(type(b) is not int):
        raise TypeError("b must be an integer")

    return (a + b)
