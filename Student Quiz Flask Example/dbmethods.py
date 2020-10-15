#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 09:28:25 2018

@author: ntcrwlr77
"""
import sqlite3 as s3
from sqlite3 import Error

def create_connection():
    """  Create the connection
    Args:
        None
    Returns:
        conn      a connection to the database
    Examples:
        >>>create_connection()
    """
    try:
        conn = s3.connect("hw13.db")
        return conn
    except Error as e:
        print e

def create_tables(conn):
    """  Create the table
    Args:
        conn(Connection)   connection to the database
    Returns:
        None
    Examples:
        >>>create_tables(conn)
    """
    try:
        # Create the Students table
        conn.execute("""DROP TABLE IF EXISTS Students;""")
        conn.execute("""CREATE TABLE IF NOT EXISTS Students(stud_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                            first_name TEXT, last_name TEXT); """)

        #Create the quizzes table
        conn.execute("""DROP TABLE IF EXISTS Quizzes;""")
        conn.execute("""CREATE TABLE IF NOT Exists Quizzes(quiz_id INTEGER PRIMARY KEY AUTOINCREMENT, subject TEXT,
                                                           number_of_questions TEXT,
                                                            date_of_quiz TEXT);""")

        #Create the Results table
        conn.execute("DROP TABLE IF EXISTS Results;")
        conn.execute("""CREATE TABLE IF NOT Exists Results(res_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                           stu_id INTEGER,quiz_id INTEGER,
                                                           score INTEGER); """)
    except Error as e:
        print e        

def delete_quiz(conn, quiz_id):
    """  Delete a quiz from the table
    Args:
        conn(Connection)   connection to the database
        quiz_id(int)       quiz id
    Returns:
        None
    Examples:
        >>>delete_quiz(conn, quiz_id)
    """
    sql_delete_quiz = "DELETE FROM Quizzes WHERE quiz_id = " + str(quiz_id)
    sql_delete_results = "DELETE FROM Results WHERE quiz_id = "  + str(quiz_id)

    try:
        cur = conn.cursor()
        cur.execute(sql_delete_quiz)
        conn.commit()
        cur.execute(sql_delete_results)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print e

def delete_student(conn, stud_id):
    """  Delete student from the table
    Args:
        conn(Connection)   connection to the database
        stud_id(int)       student id
    Returns:
        None
    Examples:
        >>>delete_student(conn, stud_id)
    """    
    sql_del_stud = "DELETE FROM Students WHERE stud_id = " + str(stud_id)
    sql_del_res = "DELETE FROM Results WHERE stu_id = " + str(stud_id)

    try:
        cur = conn.cursor()
        cur.execute(sql_del_stud)
        conn.commit()
        cur.execute(sql_del_res)
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print e

def insert_student(conn, first_name, last_name):
    """  Insert student into the table
    Args:
        conn(Connection)    connection to the database
        first_name(string)  first_name
        last_name(string)   last name
    Returns:
        None
    Examples:
        >>>insert_student(conn, first_name, last_name)
    """
    sql_load = "INSERT INTO students (first_name, last_name) VALUES(?,?)"

    try:
        cur = conn.cursor()
        cur.execute(sql_load,(first_name, last_name))
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print e
 
def insert_grade(conn, student_id, quiz_id, score):
    """  Insert grade into the table
    Args:
        conn(Connection)      connection to the database
        student_id(int)       student id
        quiz_id(int)          quiz id
    Returns:
        None
    Examples:
        >>>insert_grade(conn, student_id, quiz_id, score)
    """    
    sql_load = "INSERT INTO results (stu_id, quiz_id, score)  VALUES(?, ?, ?)"

    try:
        cur = conn.cursor()
        cur.execute(sql_load, (student_id, quiz_id, score))
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print e

def insert_quiz(conn, subject, num_q, date_of_quiz):
    """  Insert quiz into the table
    Args:
        conn(Connection)      connection to the database
        subject(int)          subject
        num_q(int)            number of questions
    Returns:
        None
    Examples:
        >>>insert_quiz(conn, subject, num_q, date_of_quiz)
    """
    sql_load = "INSERT INTO Quizzes (subject, number_of_questions, date_of_quiz) VALUES(?,?,?)"  

    try:
        cur = conn.cursor()
        cur.execute(sql_load,(subject, num_q, date_of_quiz))
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print e

def select_students():
    """  Select students from the table
    Args:
        None
    Returns:
        Rows object
    Examples:
        >>>select_students()
    """
    try:
        conn = s3.connect('hw13.db')
        conn.row_factory = s3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM students")
        rows = cur.fetchall();
        return rows
    except Error as e:
        print e

def select_quizzes():
    """  Select quizzes from the table
    Args:
        None
    Returns:
        Rows object
    Examples:
        >>>select_quizzes()
    """
    try:
        conn = s3.connect('hw13.db')
        conn.row_factory = s3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM quizzes")
        rows = cur.fetchall();
        return rows
    except Error as e:
        print e

def select_grades_quiz_info(id):
    """  Select grade info from the table
    Args:
        id(integer)
    Returns:
        Rows object
    Examples:
        >>>select_grades_quiz_info(id)
    """
    query_str = "SELECT Quizzes.quiz_id AS ID, Quizzes.subject AS Subject, Results.score AS Score, Quizzes.date_of_quiz AS Date FROM Quizzes JOIN Results ON Quizzes.quiz_id = Results.quiz_id WHERE Results.stu_id ={} ".format(id) 
    try:
        conn = s3.connect("hw13.db")
        conn.row_factory = s3.Row
        cur = conn.cursor()
        cur.execute(query_str)
        rows = cur.fetchall();
        return rows
    except Error as e:
        print e

def select_grades(id):
    """  Select grades info from the table
    Args:
        id(integer)
    Returns:
        Rows object
    Examples:
        >>>select_grades_quiz_info(id)
    """
    query_str = "SELECT * FROM results WHERE stu_id = " + str(id)

    try:
        conn = s3.connect("hw13.db")
        conn.row_factory = s3.Row
        cur = conn.cursor()
        cur.execute(query_str)
        rows = cur.fetchall();
        return rows
    except Error as e:
        print e

def select_all_grades(id):
    """  Select all grades info from the table
    Args:
        None
    Returns:
        Rows object
    Examples:
        >>>select_all_grades(id)
    """
    query_str = "SELECT stu_id, score FROM results WHERE quiz_id = " + str(id)

    try:
        conn = s3.connect("hw13.db")
        conn.row_factory = s3.Row
        cur = conn.cursor()
        cur.execute(query_str)
        rows = cur.fetchall();
        return rows

    except Error as e:
        print e
