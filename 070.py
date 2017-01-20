# ! /usr/bin/env python3
#
# Print every two letters pairs, without duplicates
#
# Introduces: for, if.
#
# Author(s): Julien Palard
# Instructions
#
# Provide a script printing every possible pairs of two letters, only lower case, one by line, ordered alphabetically, but that skip duplicates, such as 'aa', 'bb', etc...
#
# So your output should look like:
#
# $ python3 solution.py
# ab
# ..
# az
# ba
# bc
# ,,
# zy

import string

a = string.ascii_lowercase
for i in a:
    for j in a:
        if i == j:
            pass
        else:
            print(i+j)
