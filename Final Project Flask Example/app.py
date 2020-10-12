#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 00:20:06 2018

@author: ntcrwlr77
"""
from flask import render_template, request, flash, redirect, url_for, session

from config import app
from db_setup import init_db,insert_users, insert_contact, insert_course_info, insert_registered, insert_available
from forms import LoginForm, Update_Info
from models import User, Contact_Info, Registered_Courses, Course_Info, Available_Courses
from config import db
from sqlalchemy_utils import database_exists



@app.route('/', methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    """  main entry point for the application
    Args:
        None
    Returns:
        None
    Examples:
        >>>
    """
    form = LoginForm()

    if request.method == 'GET':
        return render_template('login.html', form=form)
    else: 
        if form.validate_on_submit():
            user= User.query.filter_by(email=form.username.data, 
                                       password=form.password.data).first()

            if user is not None:
                session["user_id"] = user.id
                session["logged_in"] = True
                session["name"] = user.name
                return redirect(url_for('main_page'))
            else:
                flash("User not found!")
                return render_template('login.html', form=form)

@app.route('/log_out',methods=['GET','POST'])
def log_out():
    """  Logout route
    Args:
        None
    Returns:
        None
    Examples:
        >>>
    """
    session.pop('logged_in', None)
    session.pop('user_id', None)
    session.pop('name', None)

    flash("You are now logged out.")
    return redirect(url_for('index'))

@app.route('/main_page', methods=['GET','POST'])
def main_page():
    """ main page route
    Args:
        None
    Returns:
        None
    Examples:
        >>>
    """
    flash("You are logged in! ")
    return render_template('dashboard.html')

@app.route('/register_classes', methods=['GET','POST'])
def register_classes():
    """  Register for courses
    Args:
        None
    Returns:
        None
    Examples:
        >>>
    """
    departments = ['MATH','CS','ART','HIST']

    if request.method == "GET":
       return render_template ('Register_Courses.html', departments=departments)
    elif request.method == "POST":
        if request.form.get("search_classes") != None:
            dpt = request.form["department"]
            classes = db.session.query(Available_Courses.id, Available_Courses.course_id,Course_Info.dept, Course_Info.courseNum, Course_Info.courseTitle).join(Course_Info, Available_Courses.course_id == Course_Info.id).filter(Course_Info.dept == dpt)
            flash("Class search completed.")
            return render_template ('Register_Courses.html', departments=departments, classes=classes)
        else:
            course = request.form["Register_class"]
            db.session.add(Registered_Courses(session['user_id'], course))
            db.session.commit()
            flash("Class added to the schedule.")
            return redirect(url_for('view_schedule'))
    else:
        return "Problem with the application"

@app.route('/view_contact', methods=['GET','POST'])
def view_contact():
   """  view contact information route
    Args:
        None
    Returns:
        None
    Examples:
        >>>
    """  
   form = Update_Info()
   ses = str(session['user_id'])
   yorn = session['logged_in']
   nme = session['name']

   contact = Contact_Info.query.filter_by(user_id  = int(ses)).first()

   if request.method == "GET":
       return render_template ('view_contact.html', sess=ses, logged_in = yorn,
                               loginname = nme, name= nme, 
                               address=contact.address,
                               city=contact.city, state=contact.state, 
                               phone = contact.phone, form=form)
   elif request.method == "POST":
       addr = form.address.data
       cty = form.city.data
       stte = form.state.data
       phne = form.phone.data

       contact.address = addr
       contact.city = cty
       contact.state = stte
       contact.phone = phne

       db.session.commit()
       db.session.close()

       flash("You have changed your contact information successfully ")
       return redirect(url_for('view_contact'))
   else:
       return "There has been an error!"

@app.route('/view_schedule', methods=['GET','POST'])
def view_schedule():
    """  view course schedule route
    Args:
        None
    Returns:
        None
    Examples:
        >>>
    """
    ses = session['user_id']

    classes =  db.session.query(Registered_Courses.id, Registered_Courses.course_id, Course_Info.dept, Course_Info.courseNum, Course_Info.courseTitle).join(Course_Info, Registered_Courses.course_id == Course_Info.id).filter(Registered_Courses.user_id == ses)

    if request.method == "GET":
        return render_template ('view_schedule.html', classes=classes)
    else:
        if request.form.get('delete_all_classes'):
            db.session.query(Registered_Courses).filter(Registered_Courses.user_id == ses).delete()
            db.session.commit()
            flash ("All classes have been successfully dropped!")
        else:
            id_num = request.form.get('delete_class')
            Registered_Courses.query.filter(Registered_Courses.id == id_num).delete()
            db.session.commit() 
            flash ("The class has been successfully dropped!")
        return redirect(url_for('view_schedule'))

def intialize_database():
    """  Intializes the database for the application
    Args:
        None
    Returns:
        None
    Examples:
        >>>
    """
    if database_exists("sqlite:///studentadmin.db") is False:
        init_db()
        insert_users()
        insert_contact()
        insert_course_info()
        insert_registered()
        insert_available()

if __name__ == '__main__':
    intialize_database()   
    app.run(debug=False)