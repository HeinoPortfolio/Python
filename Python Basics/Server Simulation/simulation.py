#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" File to open and simualte a server request"""

import argparse
import urllib2
import csv


class Queue:
    """ A class to create a Queue"""

    len_of_q = 0

    def __init__(self):
        """  Constructor of the class
        Args:
            None
        Examples:
        """
        self.items = []

    def is_empty(self):
        """  Check to see if the Queue is empty
        Args:
            None

        Returns:
           True or False      True if queue is empty False otherwise
        Examples:
        >>>myqueue.is_empty()
         False

        """
        return self.items == []

    def enqueue(self, item):
        """  Adds item to the Queue
        Args:
            item(various)       item to be added to the Queue

        Returns:
            None

        Examples:
        >>> myqueue.enqueue(item)
        """
        self.items.insert(0, item)
        self.len_of_q = self.len_of_q + 1

    def dequeue(self):
        """  Remove item from the Queue
        Args:
            None

        Returns:
            item (various)    item removed from queue

        Examples:
        >>> myqueue.dequeue()
        """
        self.len_of_q = self.len_of_q - 1
        return self.items.pop()

    def size(self):
        """  Returns the size of the Queue
        Args:
            None

        Returns:
            int        size of the queue

        Examples:
        >>> myqueue.size()
        """
        return len(self.items)

    def length_of_q(self):
        """  Returns the size of the Queue
        Args:
            None

        Returns:
            int             length of the queue

        Examples:
        >>> myqueue.enqueue(item)
        """
        return self.len_of_q

class Request:
    """ Models a server request object """
    time_in = 0
    image = ""
    process_time = 0
    time_stamp = 0

    def __init__(self, time_in, image, proc_time):
        """  Constructor of the class
        Args:
            None
        Examples:
        """
        self.time_in = time_in
        self.image = image
        self.process_time = proc_time

    def get_time_in(self):
        """  Gets time that the request has arrived
        Args:
            None

        Returns:
           int      time the request has entered.
        Examples:
        >>>myrequest.get_time_in()
        8
        """
        return self.time_in

    def get_image(self):
        """  Gets image that is associated with this request
        Args:
            None

        Returns:
           strng      image associated with the request.
        Examples:
        >>>myrequest.get_image()

        """
        return self.pages

    def get_process_time(self):
        """  Gets how long the process takes to run.
        Args:
            None

        Returns:
           int      process run time
        Examples:
        >>>myrequest.get_process_time()
        3
        """
        return self.process_time

    def wait_time(self):
        """  Gets how long the process takes to run.
        Args:
            None

        Returns:
           int      process run time
        Examples:
        >>>myrequest.wait_time()
        3
        """
        return self.process_time

    def display_request(self):
        """  Displays the request
        Args:
            None

        Returns:
            None
        Examples:
        >>>myrequest.display_request()
        """
        print self.time_in, self.image, self.process_time

class Server:
    """ A server object"""

    def __init__(self):
        """  Constructor of the class
        Args:
            None
        Examples:
        """
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        """  Ticks time off
        Args:
            None
        Examples:
        """
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        """  Checks to see if the server is busy
        Args:
            None

        Returns:
            True or False      True if busy
        Examples:
        """
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self, new_task):
        """  Get next task in the queue
        Args:
            new_task(Request)   next task in the queue
        Examples:
        """
        self.current_task = new_task
        self.time_remaining = new_task.get_process_time()


def downloadData(url):
    """  Method to open file and return  a handler
    Args:
        url(string):    string containing the url of the file

    Return:
       fileIn(file):  file with data
    Example:
    >>> downloadData(url)
    """

    file_in = urllib2.urlopen(url)
    return file_in

def simulateOneServer(request_queue):
    """    Method to process a request queue and return average wait time.
    Args:
        inputfile(file):    string containing the url of the file

    Return:

    Example:
    >>>
    """
    latency_time = 0
    process_prev = 0
    time_cur = 0
    time_prev = 0

    waiting_times = []
    lab_server = Server()

    while(not request_queue.is_empty()):
        if (not lab_server.busy()):
            next_task = request_queue.dequeue()
            time_cur = next_task.get_time_in()
            process_cur = next_task.get_process_time()
            if time_cur == time_prev:
                latency_time = process_prev
            elif time_cur - time_prev > 1:
                latency_time = process_prev - (time_cur - time_prev)
            else:
                latency_time = process_prev
            time_prev = time_cur
            process_prev = process_cur

            waiting_times.append(latency_time)
            lab_server.start_next(next_task)

        lab_server.tick()

    average_wait = float(sum(waiting_times)) / len(waiting_times)
    print("Average Wait %6.5f secs %3d tasks remaining,") % (average_wait, request_queue.size())

    return request_queue

def simulateManyServers(request_queue, number_of_servers):
    """    Method to process a request queue and return average wait time
           using multiple servers.
    Args:
        inputfile(file):    string containing the url of the file

    Return:

    Example:
    >>>
    """
    server_list = []
    waiting_times = []

    for index in range(number_of_servers):
        server_queue = Queue()
        server_list.append(server_queue)

    # send requests to each server.
    index = 0
    while (not request_queue.is_empty()):
        request = request_queue.dequeue()
        if index == (number_of_servers - 1):
            server_list[index].enqueue(request)
            index = 0
        else:
            server_list[index].enqueue(request)
            index += 1

    #process the  requests in the servers
    process_prev = 0
    time_cur = 0
    time_prev = 0
    index = 0
    while index < number_of_servers:
        while (not server_list[index].is_empty()):
            request = server_list[index].dequeue()
            time_cur = request.get_time_in()
            process_cur = request.get_process_time()

            if time_cur == time_prev:
                latency_time = process_prev
            elif time_cur - time_prev > 1:
                if process_prev > (time_cur- time_prev):
                    latency_time = (process_prev - (time_cur - time_prev))
                else:
                    latency_time = 0
            elif time_cur - time_prev == 1:
                latency_time = process_prev - 1
            else:
                latency_time = process_prev

            time_prev = time_cur
            process_prev = process_cur
            waiting_times.append(latency_time)

        index += 1

    average_wait = float(sum(waiting_times)) / len(waiting_times)
    print("Average Wait %6.5f secs %3d tasks remaining,") % (average_wait, request_queue.size())

def main(URL, NUMSERVERS):
    """  Main driver of the program
        Args:
            URl(string)         file name to get the data from
            NUMSERVERS(int)     number of servers
        Examples:
    """
    file_in = downloadData(URL)

    read_row = csv.reader(file_in)
    request_queue = Queue()

    for index, row in enumerate(read_row):
        new_request = Request(int(row[0]), row[1], int(row[2]))
        request_queue.enqueue(new_request)

    if NUMSERVERS is None:
        print "No servers entered Defaulting to one. \n"
        simulateOneServer(request_queue)
    else:
        print "\nMore than one server entered. \n"
        simulateManyServers(request_queue, NUMSERVERS)

if __name__ == "__main__":

    # Retrieve the url from the command line and number of servers.
    PARSER = argparse.ArgumentParser(description="Assginment 5")

    PARSER.add_argument("--file", metavar='FILENAME', type=str, help="File name for data", required=False)
    PARSER.add_argument('--servers', metavar='NUMSERVERS', type=int, help='Number of servers', required=False)

    #print vars(PARSER.parse_args())['url']

    args = vars(PARSER.parse_args())

    if args['file'] is None:
        print"No URL given"
        print "Program terminating!"
        exit()
    else:
        main(args['file'], args['servers'])
