#! /usr/bin/env python3

# SUM of pairs numbers <= 100
#
# Introduces: variables, for.
#
# Author(s): Julien Palard
# Instructions
#
# Provide a script that prints the sum of every even numbers in the range [0; 100]

def iseven(given):
    """
    Tests if a given number is even (True) or not (False)
    """
    return (given % 2) == 0

sum = 0
for i in range(1, 101):
    if(iseven(i)):
        sum += i
print(sum)
