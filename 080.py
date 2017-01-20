# ! /usr/bin/env python3
#
# Print combinations of two lower case letters
#
# Introduces: strings, for, if.
#
# Author(s): Julien Palard
# Instructions
#
# Print every possible combinations of 2 lowercase letters, one by line.
#
# A combination skips a lots of pairs, make sure you understand : https://en.wikipedia.org/wiki/Combination
# ```python
# $ python3 solution.py
# ab
# ac
# ad
# ae
# af
# ag
# ah
# ai
# aj
# ak
# ...
# vw
# vx
# vy
# vz
# wx
# wy
# wz
# xy
# xz
# yz
# ```

import string

a = string.ascii_lowercase
b = []
for i in a:
    for j in a:
        if i == j:
            pass
        else:
            k = i + j
            l = j + i
            if k not in b and l not in b:
                b.append(k)
for i in b:
    print(i)
