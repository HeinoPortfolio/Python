#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 06:24:22 2018

@author: ntcrwlr77
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    
    username = StringField('Username', validators=[DataRequired()], 
                                                   default="test1@gmail.net")
    #password = StringField('Password', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class Update_Info(FlaskForm):

    address = StringField('Address')
    city = StringField('City')
    state = StringField('State')
    phone = StringField('Phone')
    submit = SubmitField('Submit Changes')
    
    
 