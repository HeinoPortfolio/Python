#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 09:25:26 2018

@author:Heino
"""


import re
import csv
import os
from flask import Flask
from flask import flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = 'assignment'

todolist = []

def initiate_todo():
    """  Iniitate the application from a file

    Args:
        todolist (list)

    Returns:
        todolist(list)       todo tasks appendended to it

    Examples:
    >>>initiate_todo()
    """
    if os.path.exists('todo.csv'):
        #read from a file
        with open('todo.csv', mode='r') as todo_file:
            todo_reader = csv.DictReader(todo_file)
            for row in todo_reader:
                todolist.append(row)
    else:
        print "File does not exist!"

@app.route('/delete_item', methods=['GET', 'POST'])
def  delete_item():
    """  Delete an items from the list

    Args:
        todolist (list)

    Returns:
        todolist(list)       todo tasks with item deleted

    Examples:
    >>>delete_item()
    """
    found = True
    index = 0
    task = request.form['todo'].strip()

    while found:
        if todolist[index]['todo'] == task:
            del todolist[index]
            flash('The selected item has been deleted!')
            return redirect(url_for('index'))
        index += 1

@app.route('/clear', methods=['GET', 'POST'])
def clear():
    """  Clears the list

    Args:
        todolist (list)

    Returns:
        todolist(list)       Cleared todo list

    Examples:
    >>>clear()
    """
    del todolist[:]
    flash('List has been cleared!')

    return redirect(url_for('index'))

@app.route('/save', methods=['GET', 'POST'])
def save():
    """  save the list

    Args:
        todolist (list)

    Returns:
        todolist(list)       Todo item is saved to the list

    Examples:
    >>>save()
    """
    with open('todo.csv', mode='w') as todo_file:
        fieldnames = ['todo', 'email', 'priority']
        writer = csv.DictWriter(todo_file, fieldnames=fieldnames)
        writer.writeheader()

        for item in todolist:
            writer.writerow({'todo': item['todo'], 'email': item['email'], 'priority': item['priority']})

    todo_file.close()

    flash('To-do list saved!')
    return redirect(url_for('index'))

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    """  submit the list

    Args:
        todolist (list)

    Returns:
        todolist(list)       New item submitted to the list

    Examples:
    >>>submit()
    """

    email = request.form['email'].strip()
    task = request.form['task'].strip()
    priority1 = request.form['priority']

    regex = r"^\S+@\S+\.\S+$"

    #check the email for valididty
    if re.search(regex, email):
        #insert into todo list
        task = {'todo': task, 'email': email, 'priority': priority1}
        todolist.append(task)
        flash('To-do added to the list!')
    else:
        flash('Invalid email address.')

    return redirect(url_for('index'))

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    """  main point for the application

    Args:
        todolist (list)

    Returns:
        todolist(list)       todo tasks with item deleted
    Examples:
    >>>index()
    """
    return render_template('index.html', title='Week 11 Assignment', todolist=todolist)

if __name__ == '__main__':

    initiate_todo()

    app.run()


