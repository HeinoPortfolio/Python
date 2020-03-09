#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 05:49:24 2018

@author: ntcrwlr77
"""
class ConversionNotPossible(Exception):
    """Class for a custom exception for impossible conversion"""
    pass


CONVERSION_FACTORS = {'ctof': (0, 1.8, 32),
                          'ctok': (0, 1, 273.15),
                          'ctoc': (0, 1, 0),
                          'ftoc': (-32, .555555556, 0),
                          'ftok': (459.67, .555555556, 0),
                          'ftof': (0, 1, 0),
                          'ktoc': (-273.15, 1, 0),
                          'ktof': (0, 1.8, -459.67),
                          'ktok': (0, 1, 0),
                          'mitoy': (0, 1760, 0),
                          'mitokm': (0, 1.60934, 0),
                          'mitomi': (0, 1, 0),
                          'mitom': (0, 1609.34, 0),
                          'ytomi': (0, .000568182, 0),
                          'ytokm': (0, .000914, 0),
                          'ytoy': (0, 1, 0),
                          'ytom': (0, 0.9144, 0),
                          'kmtoy': (0, 1093.61, 0),
                          'kmtomi': (0, .621371, 0),
                          'kmtokm': (0, 1, 0),
                          'kmtom': (0, 1000, 0),
                          'mtom': (0, 1, 0),
                          'mtomi': (0, 0.000621371, 0),
                          'mtoy': (0, 1.09361, 0)}

def convert(fromUnit, toUnit, value):
    """  Generic way to convert between units
        Args:
            fromUnit(string)   string to convert from
            toUnit(string)     string t convert to
        Returns:
           float      Tr
        Examples:
        >>>convert('k','c', 0)
         32

    """
    

    conv = fromUnit + "to" + toUnit
    try:
        if conv in CONVERSION_FACTORS:
            result = ((value + CONVERSION_FACTORS[conv][0]) *
                      CONVERSION_FACTORS[conv][1] + CONVERSION_FACTORS[conv][2])
            return round(result, 2)
        else:
            raise ConversionNotPossible
    except ConversionNotPossible:
        print ("Conversion error! Unable to convert with given units.")
