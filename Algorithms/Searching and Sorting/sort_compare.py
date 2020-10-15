#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""File to compare the sort times of various sort mthods"""

import time
import random

def insertion_sort(a_list):
    """  Insertion sort method
    Args:
        a_list(list):        list of the items to be sorted

    Return:
        a_listfound(list):   sorted list
        end-start(time):     elapsed time

    Example:
    >>> insertion_sort(a_list)
    """

    start = time.time()

    for index in range(1, len(a_list)):

        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:

            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value

    end = time.time()

    end_time = end - start

    return a_list, end_time

def shell_sort(a_list):
    """  Shell sort method
    Args:
        a_list(list):        list of the items to be sorted

    Return:
        a_listfound(list):   sorted list
        end-start(time):     elapsed time

    Example:
    >>> shell_sort(a_list)
    """

    start = time.time()
    sublist_count = len(a_list) // 2

    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)

        #print("After increment of size", sublist_count, "The list is ", a_list)

        sublist_count = sublist_count // 2

    end = time.time()

    return a_list, end - start

def gap_insertion_sort(a_list, start, gap):
    """  method for insertion sort

    Args:
        a_list(list):    list to sorted
        start(start time): start time of algorithm

    Return:
       None

    Example:
    >>> gap_insertion_sort(a_list, start, gap)
    """


    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:

            a_list[position] = a_list[position - gap]
            position = position - gap
            a_list[position] = current_value

def python_sort(py_list):
    """  Python sort method wrapper function
    Args:
        a_list(list):        list of the items to be sorted

    Return:
        a_listfound(list):   sorted list
        end-start(time):     elapsed time

    Example:
    >>> python_sort(a_list)
    """

    start = time.time()
    py_list.sort()
    end = time.time()

    return py_list, end - start


def main():
    """  Main entry point for the program
    Args:
        None

    Return:
       None

    Example:
    >>> main()
    """

    key_values = ('ins_500', 'shell_500', 'python_500', 'ins_1000'
                  , 'shell_1000', 'python_1000', 'ins_10000'
                  , 'shell_10000', 'python_10000')

    time_dict = dict.fromkeys(key_values, 0)

    counter = 0

    while counter < 100:
 
        # create a random list of 500 numbers
        random_list_500 = random.sample(xrange(500), 500)

        insert_list = random_list_500[:]
        shell_list = random_list_500[:]
        python_list = random_list_500[:]


        time_dict['ins_500'] = time_dict['ins_500'] + insertion_sort(insert_list)[1]
        time_dict['shell_500'] = time_dict['shell_500'] + shell_sort(shell_list)[1]
        time_dict['python_500'] = time_dict['python_500'] + python_sort(python_list)[1]



        # create a random list of 1000 numbers
        random_list_1000 = random.sample(xrange(1000), 1000)

        insert_list = random_list_1000[:]
        shell_list = random_list_1000[:]
        python_list = random_list_1000[:]

        
        time_dict['ins_1000'] = time_dict['ins_1000'] + insertion_sort(insert_list)[1]
        time_dict['shell_1000'] = time_dict['shell_1000'] + shell_sort(shell_list)[1]
        time_dict['python_1000'] = time_dict['python_1000'] + python_sort(python_list)[1]

        # create a random list of 10000 numbers
        random_list_10000 = random.sample(xrange(10000), 10000)
        
        insert_list = random_list_10000[:]
        shell_list = random_list_10000[:]
        python_list = random_list_10000[:]


        time_dict['ins_10000'] = time_dict['ins_10000'] + insertion_sort(insert_list)[1]
        time_dict['shell_10000'] = time_dict['shell_10000'] + shell_sort(shell_list)[1]
        time_dict['python_10000'] = time_dict['python_10000'] + python_sort(python_list)[1]

        print "Finished sorting list {%d}" % counter   

        counter += 1

    print "\nFor 500 items:\n"
    print "Insertion Sort took %10.7f" % float(time_dict['ins_500'] / 100) + ' seconds to run, on average.'
    print "Shell Sort took %10.7f" % float(time_dict['shell_500'] / 100) + ' seconds to run, on average.'
    print "Python Sort took %10.7f" % float(time_dict['python_500'] / 100) + ' seconds to run, on average.'

    print "\nFor 1000 items:\n"
    print "Insertion Sort took %10.7f" % float(time_dict['ins_1000'] / 100) + ' seconds to run, on average.'
    print "Shell Sort took %10.7f" % float(time_dict['shell_1000'] / 100) + ' seconds to run, on average.'
    print "Python Sort took %10.7f" % float(time_dict['python_1000'] / 100) + ' seconds to run, on average.'

    print "\nFor 10000 items:\n"
    print "Insertion Sort took %10.7f" % float(time_dict['ins_10000'] / 100) + ' seconds to run, on average.'
    print "Shell Sort took %10.7f" % float(time_dict['shell_10000'] / 100) + ' seconds to run, on average.'
    print "Python Sort took %10.7f" % float(time_dict['python_10000'] / 100) + ' seconds to run, on average.'

    print "\n\n"


if __name__ == "__main__":

    main()


