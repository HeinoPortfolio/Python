#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 22:31:59 2018

@author: ntcrwlr77
"""

from flask import Flask
from flask import flash, redirect, render_template, request,session,  url_for
import dbmethods as dbm
import sqlite3 as s3

app = Flask(__name__)
app.secret_key = 'assignment'

USERNAME = 'admin'
PASSWORD = 'password'
GUEST = 'Guest'
ANON = 'anon'

@app.route('/student/add', methods=['POST', 'GET'])
def add_student():
    """  Add student to the roster
    Args:
        None
    Returns:
    Examples:
        >>>add_student()
    """
    if 'logged_in' in session:
        if request.method == 'POST':        
            first_name = request.form['first_name']
            last_name = request.form['last_name']

            #Insert new student into the database
            conn = s3.connect('hw13.db')
            dbm.insert_student(conn, first_name, last_name)
            conn.close()

            flash("Successfully added the student!")
            return redirect(url_for('dashboard'))
        else:
            return render_template("add_student.html")
    else:
        flash("You are not logged in you cannot view this page!")
        return render_template('login.html', title="Login In Screen")

@app.route('/quiz/add', methods=['POST', 'GET'])
def add_quiz():
    """  Add student to the roster
    Args:
        None
    Returns:
    Examples:
        >>>add_quiz()
    """
    months = ['January', 'February','March', 'April', 'May', 'June', 'July', 
              'August', 'September','October','November', 'December']

    prefix = ""

    if 'logged_in' in session:
        if request.method == 'POST':
            month = request.form['month']
            day = request.form['day']
            year = request.form['year']
            subject = request.form['subject']
            num_q = request.form['questions']
            
            if day == '1':
                prefix = 'st'
            elif day == '2':
                prefix = 'nd'
            elif day == '3':
                prefix = 'rd'
            else:
                prefix = 'th'
            date1 = month + ", " + day + prefix + ", " + year

            #insert the quiz into the database
            conn = s3.connect('hw13.db')
            dbm.insert_quiz(conn, subject, num_q, date1)
            flash("Successfully added the quiz!")
            return redirect(url_for('dashboard'))
        else:
            return render_template("add_quiz.html", months = months)
    else:
        return render_template("add_quiz.html", months=months)

@app.route('/results/add', methods=['POST', 'GET'])
def add_quiz_grade():
    """  Add quiz grade
    Args:
        None
    Returns:
    Examples:
        >>>add_quiz()
    """

    students = dbm.select_students()
    quizzes = dbm.select_quizzes()

    if 'logged_in' in session:
        if request.method == "POST":
            student_id = request.form.get('student_select')
            quiz_id = request.form.get('quiz_select')
            score = request.form['grade']

            #Insert Grade into table
            conn = s3.connect('hw13.db')
            dbm.insert_grade(conn, student_id, quiz_id, score)

            flash("Successfully added the quiz grade!")
            return redirect(url_for('dashboard'))
        else:
            return render_template("add_quiz_grade.html", students=students, quizzes=quizzes)
    else:
        return render_template("add_quiz_grade.html", students=students, quizzes=quizzes)

@app.route('/delete', methods=['POST', 'GET'])
def delete_data():
    """  Delete data
    Args:
        None
    Returns:
    Examples:
        >>>delete_data()
    """
    quizzes = dbm.select_quizzes()
    students = dbm.select_students()

    if request.method == 'POST':
        if request.form['delete'] == 'Delete Quiz':
            quiz_id = request.form['quiz_select']
            conn = dbm.create_connection()
            dbm.delete_quiz(conn,quiz_id)
            flash("Quiz has been deleted")
        elif request.form['delete'] == 'Delete Student':
            stud_id = request.form['student_select']
            conn = dbm.create_connection()
            dbm.delete_student(conn,stud_id)
            flash("Student has been deleted")
        return redirect(url_for('dashboard'))
    return render_template("delete.html", quizzes=quizzes, students=students)

@app.route('/quiz/<id>', methods=['POST', 'GET'])
def view_anon(id=None):
    """  View grades anononymously
    Args:
        None
    Returns:
    Examples:
        >>>view_anon(id=None)
    """
    quizzes = dbm.select_quizzes()

    if "anon" in session or "logged_in" in session:
        if request.method == "GET":
            scores = dbm.select_all_grades(id)
            flash("Grades Retrieved!")
            return render_template("anon_view.html", quizzes=quizzes, scores=scores)
    return render_template("anon_view.html", quizzes=quizzes)

@app.route('/student/<id>', methods=['POST', 'GET'])
def view_quizzes(id):
    """  View quizzes
    Args:
        None
    Returns:
    Examples:
        >>>view_quizzes(id)
    """
    if "logged_in" in session:
        grades = dbm.select_grades_quiz_info(id)
        if len(grades) != 0:
            flash("Grades Retrieved")
            return render_template("view_grades.html", grades=grades)
        else:
            flash("No Results!")
            return render_template("view_grades.html")

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    """  Dasboard for the application
    Args:
        None
    Returns:
    Examples:
        >>>view_anon(id=None)
    """
    if session['logged_in'] is True:
        rows = dbm.select_students()
        quizzes = dbm.select_quizzes()
        return render_template("dashboard.html",title='Dashboard' ,rows=rows, quizzes=quizzes)    
    else:
        flash ("You were not logged in!")
        return render_template("login.html")
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    """  login screen
    Args:
        None
    Returns:
    Examples:
        >>>login()
    """
    if request.method == 'POST':
        if request.form['username'] == GUEST and request.form['password'] == ANON:
            session['logged_in'] = False
            flash("You are currently logged in as ****GUEST*****")
            quizzes = dbm.select_quizzes()
            return render_template("anon_view.html", title="Anonymous Grade View", quizzes=quizzes)
        elif request.form['username'] != USERNAME:
            flash("Invalid username!")
            return render_template('login.html', title="Login In Screen")
        elif request.form['password'] != PASSWORD:
            flash("Invalid password!")
            return render_template('login.html', title="Login In Screen")
        else:
            flash("You have succesfully logged in!")
            session['logged_in'] = True
            return redirect(url_for('dashboard'))

@app.route('/logout', methods=['GET', 'POST'])            
def logout():
    """  logout out of the application
    Args:
        None
    Returns:
    Examples:
        >>>logout()
    """
    session.pop('logged_in', None)
    flash("You have been logged out!")
    return redirect(url_for('index'))

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    """  index - launching point
    Args:
        None
    Returns:
    Examples:
        >>>view_anon(id=None)
    """
    return render_template('login.html', title="Login In Screen")

if __name__ == '__main__':
    
    #Initialize the tables and the database
    conn = dbm.create_connection()
    dbm.create_tables(conn)

    #Add a few test students
    dbm.insert_student(conn, 'John', 'Smith')
    dbm.insert_student(conn, 'Steve', 'Mack')

    #add a few quizzes
    dbm.insert_quiz(conn, 'Python Basics', '5', 'February, 5th, 2015')
    dbm.insert_quiz(conn, 'Computer architecture', '5', 'February, 6th, 2018')
    
    #add a few quiz grades
    dbm.insert_grade(conn, 1, 1, 85)
    dbm.insert_grade(conn, 1, 2, 65)
    dbm.insert_grade(conn, 2, 2, 70)
    dbm.insert_grade(conn, 2, 1, 90)
 
    conn.close()
 
    app.run(debug=True)
    