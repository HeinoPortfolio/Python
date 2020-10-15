#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" File to compare the run times of various search methods """

import random
import time

def sequential_search(a_list, item):
    """  Sequential sort method
    Args:
        a_list(list):    a list to be searched
        item(various):   item to be searched for

    Return:
       found(boolean):   true if found and false otherwise
        end-start(time): elapsed time

    Example:
    >>> sequential_search(a_list, item)
    """

    start = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1

    end = time.time()

    return found, end-start

def ordered_sequential_search(a_list, item):
    """  Ordered search method
    Args:
        a_list(list):    a list to be searched
        item(various):   item to be searched for

    Return:
       found(boolean):   true if found and false otherwise
        end-start(time): elapsed time

    Example:
    >>> ordered_sequential_search(a_list, item)
    """

    start = time.time()

    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1
    end = time.time()

    return found, end-start



def binary_search_iterative(a_list, item):
    """  Iterative binary search search method
    Args:
        a_list(list):    a list to be searched
        item(various):   item to be searched for

    Return:
       found(boolean):   true if found and false otherwise
        end-start(time): elapsed time

    Example:
    >>> binary_search_iterative(a_list, item)
    """

    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:    # is
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end = time.time()

    return found, end - start


def binary_search_recursive(a_list, item, start):
    """  Recursive binary search search method
    Args:
        a_list(list):     a list to be searched
        item(various):  item to be searched for
        start(time):    time the method started

    Return:
       found(boolean):   true if found and false otherwise
        end-start(time): elapsed time

    Example:
    >>> binary_search_recursive(a_list, item)
    """

    # check to see if timer has started
    if start == 0:
        start = time.time()

    if len(a_list) == 0:
        end = time.time()
        return False, end - start
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            end = time.time()
            return True, end - start
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item, start)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item, start)

def main():
    """  Main entry point for the program
    Args:
        None

    Return:
       None

    Example:
    >>> main()
    """

    key_values = ('seq_500', 'ord_500', 'bin_it_500', 'bin_rec_500', 'seq_1000'
                  , 'ord_1000', 'bin_it_1000', 'bin_rec_1000', 'seq_10000'
                  , 'ord_10000', 'bin_it_10000', 'bin_rec_10000')

    time_dict = dict.fromkeys(key_values, 0)

    counter = 0

    while counter < 100:

        # create a random list of 500 numbers
        random_list_500 = random.sample(xrange(500), 500)

        # calculate time for the sequential search
        seq_time = sequential_search(random_list_500, -1)

        # calulate time for ordered search
        # sort list first
        sorted_list_500 = sorted(random_list_500)
        ord_time = ordered_sequential_search(sorted_list_500, -1)

        #calculate time for iterative binary search
        bin_it_time = binary_search_iterative(sorted_list_500, -1)
        #print bin_it_time

        #calculate time for recursive binary search
        bin_rec_time = binary_search_recursive(sorted_list_500, -1, 0)

        time_dict['seq_500'] = time_dict['seq_500'] + seq_time[1]
        time_dict['ord_500'] = time_dict['ord_500'] + ord_time[1]
        time_dict['bin_it_500'] = time_dict['bin_it_500'] + bin_it_time[1]
        time_dict['bin_rec_500'] = time_dict['bin_rec_500'] + bin_rec_time[1]

        # create a random list of 1000 numbers
        random_list_1000 = random.sample(xrange(1000), 1000)

        # calculate time for the sequential search
        seq_time = sequential_search(random_list_1000, -1)

        # calulate time for ordered search
        # sort list first
        sorted_list_1000 = sorted(random_list_1000)
        ord_time = ordered_sequential_search(sorted_list_1000, -1)

        #calculate time for iterative binary search
        bin_it_time = binary_search_iterative(sorted_list_1000, -1)

        #calculate time for recursive binary search
        bin_rec_time = binary_search_recursive(sorted_list_1000, -1, 0)

        time_dict['seq_1000'] = time_dict['seq_1000'] + seq_time[1]
        time_dict['ord_1000'] = time_dict['ord_1000'] + ord_time[1]
        time_dict['bin_it_1000'] = time_dict['bin_it_1000'] + bin_it_time[1]
        time_dict['bin_rec_1000'] = time_dict['bin_rec_1000'] + bin_rec_time[1]


        # create a random list of 1000 numbers
        random_list_10000 = random.sample(xrange(10000), 10000)

        # calculate time for the sequential search
        seq_time = sequential_search(random_list_10000, -1)

        # calulate time for ordered search
        # sort list first
        sorted_list_10000 = sorted(random_list_10000)
        ord_time = ordered_sequential_search(sorted_list_10000, -1)

        #calculate time for iterative binary search
        bin_it_time = binary_search_iterative(sorted_list_10000, -1)

        #calculate time for recursive binary search
        bin_rec_time = binary_search_recursive(sorted_list_10000, -1, 0)

        time_dict['seq_10000'] = time_dict['seq_10000'] + seq_time[1]
        time_dict['ord_10000'] = time_dict['ord_10000'] + ord_time[1]
        time_dict['bin_it_10000'] = time_dict['bin_it_10000'] + bin_it_time[1]
        time_dict['bin_rec_10000'] = time_dict['bin_rec_10000'] + bin_rec_time[1]

        counter += 1

    print "\nFor 500 items:\n"
    print "Sequential search took %10.7f" % float(time_dict['seq_500'] / 100) + ' seconds to run, on average.'
    print "Ordered search took %10.7f" % float(time_dict['ord_500'] / 100) + ' seconds to run, on average.'
    print "Binary interative search took %10.7f" % float(time_dict['bin_it_500'] / 100) + ' seconds to run, on average.'
    print "Binary recursive search took %10.7f" % float(time_dict['bin_rec_500'] / 100) + ' seconds to run, on average.'

    print "\n\nFor 1000 items:\n"
    print "Sequential search took %10.7f" % float(time_dict['seq_1000'] / 100) + ' seconds to run, on average.'
    print "Ordered search took %10.7f" % float(time_dict['ord_1000'] / 100) + ' seconds to run, on average.'
    print "Binary interative search took %10.7f" % float(time_dict['bin_it_1000'] / 100) + ' seconds to run, on average.'
    print "Binary recursive search took %10.7f" % float(time_dict['bin_rec_1000'] / 100) + ' seconds to run, on average.'

    print "\n\nFor 10000 items:\n"
    print "Sequential search took %10.7f" % float(time_dict['seq_10000'] / 100) + ' seconds to run, on average.'
    print "Ordered search took %10.7f" % float(time_dict['ord_10000'] / 100) + ' seconds to run, on average.'
    print "Binary interative search took %10.7f" % float(time_dict['bin_it_10000'] / 100) + ' seconds to run, on average.'
    print "Binary recursive search took %10.7f" % float(time_dict['bin_rec_10000'] / 100) + ' seconds to run, on average.'

    print"\n\n"



if __name__ == "__main__":

    main()


