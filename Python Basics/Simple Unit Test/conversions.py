#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Conversion file to convert temperatures into various scales

"""


def convertCelsiusToKelvin(celsius):
    """  Convert between Celsius to Kelvin
        Args:
            celsius(float)     Celsius temperature to convert
        Returns:
           float
        Examples:
        >>>convertCelsiusToKelvin(0)
         32

    """
    return celsius + 273.15

def convertCelsiusToFahrenheit(celsius):
    """  Convert between Celsius to Farenheit
        Args:
            celsius(float)     Celsius temperature to convert
        Returns:
           float
        Examples:
        >>>convertCelsiusToFahrenheit(32)
    """
    return round((celsius * (9.0/5.0)) + 32.0, 2)

def convertFahrenheitToCelsius(fahr):
    """  Convert between Farenheit to Celsius
        Args:
            fahr(float)     Fahrenheit temperature to convert
        Returns:
           float
        Examples:
        >>>convertFahrenheitToCelsius(23)
    """
    return round((fahr - 32.0) * (5.0/9.0), 2)

def convertFahrenheitToKelvin(fahr):
    """  Convert between Farenheit to Kelvin
        Args:
            fahr(float)     Fahrenheit temperature to convert
        Returns:
           float
        Examples:
        >>>convertFahrenheitToKelvin(23)
    """
    return round((fahr + 459.67) * (5.0/9.0), 2)

def convertKelvinToFahrenheit(kelvin):
    """  Convert between Kelvin to  Farenheit
        Args:
            kelvin(float)     Kelvin temperature to convert
        Returns:
           float
        Examples:
        >>>convertKelvinToFahrenheit(23)
    """
    return round((kelvin * (9.0/5.0) - 459.67), 2)

def convertKelvinToCelsius(kelvin):
    """  Convert between Kelvin to Celsius
        Args:
            kelvin(float)     Kelvin temperature to convert
        Returns:
           float
        Examples:
        >>>convertKelvinToFahrenheit(23)
    """
    return kelvin - 273.15
