#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" A class to create a Book class with a display method 
    
"""

class Book(object):
    """ A class to create a book object"""
    author = ""
    title = ""

    def __init__(self, author, title):
        """ Constructor of class

        Args:
            author (string):  author's name
            title (string):  title of the book

        Examples:
        BOOK1=Book("John Steinbeck", "Of Mice and Men")
        """
        self.author = author
        self.title = title

    def display(self):
        """  Function to display the attributes of Book

        Args:
            book Object

        Returns:
            string with the attributes appended

        Examples:
        >>> book1.display()
        " Of Mice and Men, written by John Steinbeck"
        """
        print ('\" ' + self.title + ", written by " + self.author + '\"')


BOOK1 = Book("John Steinbeck", "Of Mice and Men")

BOOK2 = Book("Harper Lee", "To Kill a Mockingbird")

BOOK1.display()
BOOK2.display()
