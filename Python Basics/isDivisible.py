#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" a File with methods to find number of items in a list that are
    divisible by a given number
"""

def listDivide(numbers, divide=2):
    """ Function to determine how many items in a list
        are divisible by a given number

    Args:
        numbers(list):   List of numbers to searched
        divide (integer or float):  number to divide list elements by

    Returns:
        count(integer):     Number of items in the list that are divisible
                            by a given number.
    Example:
    >>> listDivide([2,4,6,8])

    """

    count = 0

    if divide != 0 and (str(divide).isdigit() or divide < 0):
        for num in numbers:
            if (str(num).isdigit() or num < 0) and num % divide == 0:
                count += 1
    return count

class ListDivideException(Exception):
    """ Class to create a used defined exception """
    pass

def testListDivide():
    """  A funcction to test the listDivide method
    Args:
        NONE

    Returns:
        NONE

    Example:
    >>> testListDivide()
    2
    5
    2
    0
    5
    3
    """
    try:
        print (listDivide([1, 2, 3, 4, 5]))
        print (listDivide([2, 4, 6, 8, 10]))
        print (listDivide([30, 54, 63, 98, 100], divide=10))
        print (listDivide([]))
        print (listDivide([1, 2, 3, 4, 5], 1))
    except:
        raise ListDivideException


testListDivide()
