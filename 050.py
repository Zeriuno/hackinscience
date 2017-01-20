# ! /usr/bin/env python3
#
# Multiples of 3 and 5
#
# Introduces: operators, range.
# Instructions
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000 and print it.

def ismultiple(param):
    """
    Returns True if the argument is a multple of 3 or 5.
    """
    return (param % 3 == 0) or (param % 5 == 0)

sum = 0
for i in range(1, 1000):
    if ismultiple(i):
        sum += i
print(sum)
