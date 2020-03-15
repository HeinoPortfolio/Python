#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 02:54:09 2018

@author: Heino
"""

import sqlite3
from sqlite3 import Error

def create_connection(db_location):
    """  Create Connection to the database
    Args:
        db_location(string)   location of the database

    Returns:
        conn(Connection)      connection to the database
    Examples:
        >>>create_connection(db_location)
    """
    try:
        conn = sqlite3.connect(db_location)
        return conn
    except Error as e:
        print e

def query_pet_db(conn, per_id):
    """  Query to get pet data the database
    Args:
        conn(Connection)   connection to the database
        per_id(int)        ID of the person to display the data
    Returns:
        None
    Examples:
        >>>cquery_pet_db(conn, per_id)
   """
    cur = conn.cursor()

    cur.execute("""SELECT  per.*, pt.* FROM person as per 
                JOIN person_pet as pp ON per.id = pp.person_id 
                JOIN pet as pt ON pt.id = pp.pet_id WHERE per.id = ?""", (per_id, ))

    rows = cur.fetchall()

    if len(rows) > 0:
        display_table_result(rows)
    else:
        print "That ID is not found in the database!"

def display_table_result(rows):
    """  Display the results set of person with that
    Args:
        rows(tuple)   rows with person and pet data

    Returns:
        None
    Examples:
        >>>dispaly_table_result(rows)
   """
    age = 0
    pet_str = ''
    pet_str2 = ''
    name = ""

    for row in rows:
        if name != (row[1] +" "+ row[2]):
            name = row[1] + " " + row[2]
            age = str(row[3])
            pet_str = name +", "+ age + " years old"
            if row[8] == 1:
                pet_str2 = name + " owned "+ row[5] + ", a "+ row[6] + ", that was " + str(row[7]) + " year old."
            else:
                pet_str2 = name + " owns " + row[5] + ", a "+ row[6] + ", that is " + str(row[7]) + " year old."
        else:
            if row[8] == 1:
                pet_str2 = pet_str2 + "\nAlso owned "+ row[5] + ", a "+ row[6] + ", that was " + str(row[7]) + " year old."
            else:
                pet_str2 = pet_str2 + "\nAlso owns " + row[5] + ", a "+ row[6] + ", that is " + str(row[7]) + " year old."
    print pet_str
    print pet_str2

def main(db):
    """  Main entry point for the program
   Args:
        db(string)   location of the database

   Returns:
        None
   Examples:
        >>>main(db)
   """
    conn = create_connection(db)

    search_id = 0

    search_id = int(raw_input("What ID would you like to look for(Enter a -1 to quit.)?"))
    while search_id is not -1:
        query_pet_db(conn, search_id)
        search_id = int(raw_input("What ID would you like to look for(Enter a -1 to quit.)?"))
    print "Program ended......."

if __name__ == "__main__":
    main('pets.db')
