#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 00:17:01 2018

@author: ntcrwlr77
"""
from config import db

class User(db.Model):

    """ A class that holds  user information name, email, and password """

    __tabelname__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, nme, email, pwrd):
        """  Initializes the User table
        Args:
            nme (string)   name of user
            email(string)  email of the student/user
        Returns:
        Examples:
                >>>
        """
        self.name = nme
        self.email = email
        self.password = pwrd

    def __repr__(self):
        """  Load person data into database tables
        Args:
            self
        Returns:
            string             
        Examples:
        >>> User:  name>
        """
        return "User: {} >".format(self.name)

class Contact_Info(db.Model):
    """ A class that holds  contact information name, email, and password """

    __tablename__ = 'contact_info'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    address = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    phone = db.Column(db.String)
  
    def __init__(self, uid, addr, cty, stte, phne):
        """  Initializes the Contact information table
        Args:
            uid (integer)  user id
            addr(string)   address of the user
            cty(string)    city of user
            stte(string)   state of user
            phne(string)   phone of user
        Returns:
        Examples:
                >>>
        """
        self.user_id = uid
        self.address = addr
        self.city = cty
        self.state = stte
        self.phone = phne

class Registered_Courses(db.Model):
    """ A class that holds courses that a student has registere for."""

    __tablename__ = 'registered'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), 
                          nullable=False)

    def __init__(self, uid, cuid):
        """  Initializes the Registered Courses table
        Args:
            uid (integer)  user ID
            cuid(integer)  course ID
        Returns:
        Examples:
                >>>
        """
        self.user_id = uid
        self.course_id = cuid
    
class Course_Info(db.Model):
    """ A class that holds course information"""

    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    dept = db.Column(db.String)
    courseNum = db.Column(db.String)
    courseTitle = db.Column(db.String)

    def __init__(self, dpt, crn, ctitle):
        """  Initializes the Course information table
        Args:
            dpt(string)      department
            crn(string)      course number
            ctitle(string)   course title
        Returns:
        Examples:
                >>>
        """
        self.dept = dpt
        self.courseNum = crn
        self.courseTitle = ctitle

class Available_Courses(db.Model):
    """ A class that holds  available courses """

    __tablename__ = 'available'

    id = db.Column(db.Integer, primary_key = True)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"),
                          nullable=False)

    def __init__(self, crs_id):
        """  Initializes the Avaiable courses table
        Args:
            crs_id (integer)  course id
        Returns:
        Examples:
                >>>
        """
        self.course_id = crs_id
