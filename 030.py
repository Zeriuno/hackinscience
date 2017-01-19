#! /usr/bin/env python3

def iseven(number):
    """
    If the number is even, returns True, otherwise returns false.
    """
    return (number %2) == 0

for i in range(1, 101):
    if iseven(i):
        print(i)
