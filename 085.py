# ! /usr/bin/env python3
#
# sort_students
#
# Introduces: function, sorted, operators.
#
# Author(s): Constance de Quatrebarbes, Antoine Mazières
# Instructions
# Exercise 1
#
# Write a function sort_a_list that takes a list as argument and return the list sorted in the descending order, such as:
#
# In [1]: from solution import sort_a_list
#
# In [2]: l = [1, 3, 2, 4, 6, 5, 9, 7]
#
# In [3]: sort_a_list(l)
# Out[3]: [9, 7, 6, 5, 4, 3, 2, 1]
#
# Exercise 2
#
# Given a list where each element is a list of a mark, and a student name, such as:
#
# [[37, 'Jeanette Wafer'], [6, 'Joshua Tran'], [85, 'Susan Maddox']]
#
# Write a function sort_by_mark that take as argument a similar list and returns it sorted by mark in the descending order. Such as:
#
# In [1]: from solution import sort_by_mark
#
# In [4]: my_class = [[6, 'Joshua Tran'], [37, 'Jeanette Wafer'], [85, 'Susan Maddox'], [84, 'Joseph Pedersen'], [12, 'Bonnie Torres'], [36, 'John Freeman'], [27, 'Betty Askins'], [22, 'Mark Osbourne'], [42, 'Lidia Robel']]
#
# In [5]: sort_by_mark(my_class)
# Out[5]:
# [[85, 'Susan Maddox'],
#  [84, 'Joseph Pedersen'],
#  [42, 'Lidia Robel'],
#  [37, 'Jeanette Wafer'],
#  [36, 'John Freeman'],
#  [27, 'Betty Askins'],
#  [22, 'Mark Osbourne'],
#  [12, 'Bonnie Torres'],
#  [6, 'Joshua Tran']]
#
# Exercise 3
#
# Write a function sort_by_name that take as argument a similar list and returns it sorted by name in the ascending order. Such as:
#
# In [1]: from solution import sort_by_name
#
# In [6]: sort_by_name(my_class)
# Out[6]:
# [[27, 'Betty Askins'],
#  [12, 'Bonnie Torres'],
#  [37, 'Jeanette Wafer'],
#  [36, 'John Freeman'],
#  [84, 'Joseph Pedersen'],
#  [6, 'Joshua Tran'],
#  [42, 'Lidia Robel'],
#  [22, 'Mark Osbourne'],
#  [85, 'Susan Maddox']]
#
# Advice
#
# Have a look at itemgetter.

def sort_a_list(alist):
    """
    Prints a sorted list.
    """
    alist.sort(reverse = True)
    print(alist)

def sort_by_mark(alist):
    """
    Sorts the given list.
    """
    alist.sort( reverse = True )
    print(alist)

def sort_by_name(alist):
    """
    Sorts the given list by name
    """

    from operator import itemgetter
    alist.sort(key= itemgetter(1))
    print(alist)
