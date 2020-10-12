#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 00:15:50 2018

@author: ntcrwlr77
"""

""" Configuration file for the application """

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///studentadmin.db'
app.secret_key = "IS211"

db = SQLAlchemy(app)