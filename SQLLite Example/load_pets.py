# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 18:14:42 2020

@author: Admin
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 00:18:51 2018

@author: ntcrwlr77
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

def create_table(conn):
    """  Create the table
    Args:
        conn(Connection)   connection to the database

    Returns:
        None
    Examples:
        >>>create_table(conn)
    """
    try:
        # Create the Person table
        conn.execute("""CREATE TABLE IF NOT EXISTS person (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER);""")

        #Create the pet table
        conn.execute("""CREATE TABLE IF NOT EXISTS pet(id INTEGER PRiMARY KEY, name TEXT,breed TEXT, age INTEGER, dead INTEGER);""")

        #Create the pet - person table
        conn.execute("""CREATE TABLE IF NOT EXISTS person_pet(person_id INTEGER, pet_id INTEGER); """)

    except Error as e:
        print e

def load_table_person_data(conn, person):
    """  Load person data into database tables
    Args:
        conn(Connection)   connection to the database
        person(list)       person data to be inserted into the table

    Returns:
        (int)              row position
    Examples:
        >>>load_table_person_data(conn, person)
    """
    print "Loading data......"

    sql_load = "INSERT INTO person(id, first_name, last_name, age ) VALUES(?,?,?,?)"

    try:
        cur = conn.cursor()
        cur.execute(sql_load, person)
        conn.commit()
        print "Finished Loading data! \n"
        return cur.lastrowid
    except Error as e:
        print e

def load_table_pet_data(conn, pet):
    """  Load pet data into database tables
    Args:
        conn(Connection)   connection to the database
        pet(list)          pet data to be inserted into the table

    Returns:
        (int)              row position
    Examples:
        >>>load_table_pet_data(conn, pet)
    """
    print "Loading data....."

    sql_load = "INSERT INTO pet (id, name, breed, age, dead ) VALUES (?, ?,?, ?, ?);"

    try:
        cur = conn.cursor()
        cur.execute(sql_load, pet)
        conn.commit()
        print "Finished Loading data! \n"
        return cur.lastrowid
    except Error as e:
        print e

def load_table_person_pet(conn, per_pet):
    """  Load person/pet data into database tables
    Args:
        conn(Connection)   connection to the database
        per_pet(list)       person/pet data to be inserted into the table

    Returns:
        (int)              row position
    Examples:
        >>>load_table_person_pet(conn, per_pet)
    """
    print "Loading data....."

    sql_load = "INSERT INTO person_pet(person_id, pet_id) VALUES (?, ?);"

    try:
        cur = conn.cursor()
        cur.execute(sql_load, per_pet)
        conn.commit()
        print "Finished Loading data! \n"
        return cur.lastrowid
    except Error as e:
        print e

def main(db_location):
    """  Main entry point for the program
    Args:
        db_location(string)   location of the database

    Returns:
        None
    Examples:
        >>>main(db_location)
    """
    conn = create_connection(db_location)

    create_table(conn)

    # person data
    person1 = (1, 'James', 'Smith', 41)
    person2 = (2, 'Diana', 'Greene', 23)
    person3 = (3, 'Sara', 'White', 27)
    person4 = (4, 'William', 'Gibson', 23)

    load_table_person_data(conn, person1)
    load_table_person_data(conn, person2)
    load_table_person_data(conn, person3)
    load_table_person_data(conn, person4)

    #pet data
    pet1 = (1, 'Rusty', 'Dalmation', 4, 1)
    pet2 = (2, 'Bella', 'Alaskan Malamute', 3, 0)
    pet3 = (3, 'Max', 'Cocker Spaniel', 1, 0)
    pet4 = (4, 'Rocky', 'Beagle', 7, 0)
    pet5 = (5, 'Rufus', 'Cocker Spaniel', 1, 0)
    pet6 = (6, 'Spot', 'Bloodhound', 2, 1)

    load_table_pet_data(conn, pet1)
    load_table_pet_data(conn, pet2)
    load_table_pet_data(conn, pet3)
    load_table_pet_data(conn, pet4)
    load_table_pet_data(conn, pet5)
    load_table_pet_data(conn, pet6)

    #pet_person data
    per_pet1 = (1, 1)
    per_pet2 = (1, 2)
    per_pet3 = (2, 3)
    per_pet4 = (2, 4)
    per_pet5 = (3, 5)
    per_pet6 = (4, 6)

    load_table_person_pet(conn, per_pet1)
    load_table_person_pet(conn, per_pet2)
    load_table_person_pet(conn, per_pet3)
    load_table_person_pet(conn, per_pet4)
    load_table_person_pet(conn, per_pet5)
    load_table_person_pet(conn, per_pet6)

    conn.close()

if __name__ == "__main__":
    main('pets.db')
       