#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Tests conversion functions

"""
import unittest
import conversions
import conversions_refactored


class knownValues(unittest.TestCase):
    """Class of known values to test against"""

    knownValuesCelsiusToKelvin = ((300.00, 573.15),
                                  (0, 273.15),
                                  (32, 305.15),
                                  (37, 310.15),
                                  (100, 373.15))

    knownValuesCelsiusToFahr = ((300, 572),
                                (0, 32),
                                (232.778, 451),
                                (26.6667, 80),
                                (7.222222222222222, 45),
                                (260, 500))

    knownValuesFahrToCelsius = ((32, 0),
                                (98.6, 37),
                                (212, 100),
                                (0, -17.78),
                                (451, 232.78))

    knownValuesFahrToKelvin = ((80, 299.82),
                               (0, 255.37),
                               (32, 273.15),
                               (212, 373.15),
                               (-2, 254.26))

    knownValuesKelvinToFahr = ((299.82, 80.01),
                               (255.37, -0.0),
                               (273.15, 32),
                               (373.15, 212),
                               (254.26, -2))

    knownValuesKelvinToCels = ((573.15, 300),
                               (273.15, 0),
                               (305.15, 32),
                               (310.15, 37),
                               (373.15, 100))

    knownValuesConvert = (('c', 'f', 0, 32),
                          ('c', 'k', 0, 273.15),
                          ('f', 'c', 0, -17.78),
                          ('f', 'k', 0, 255.37),
                          ('k', 'c', 1, -272.15),
                          ('k', 'f', 1, -457.87),
                          ('mi', 'y', 1, 1760),
                          ('mi', 'km', 1, 1.61),
                          ('y', 'mi', 1, .00),
                          ('y', 'km', 1, .00),
                          ('km', 'mi', 1, .62),
                          ('km', 'y', 1, 1093.61))

    def testConvertCelsiusToKelvin(self):
        """  Tests Conversion between Celsius to Kelvin
        Args:
           None
        Returns:
            Assertion
        """
        print("\nTesting conversion from Celsius to Kelvin. \n")
        for celsius, kelvin in self.knownValuesCelsiusToKelvin:
            print (('Testing {} convertion should be equal to {}').format(celsius, kelvin))
            result = conversions.convertCelsiusToKelvin(celsius)
            print (('The result of the conversion: {}\n').format(result))
            self.assertEqual(kelvin, result)

    def testConvertCelsiusToFahrenheit(self):
        """  Tests Conversion between Celsius to Fahrenheit
        Args:
           None
        Returns:
            Assertion
        """
        print ("\nTesting conversion from Celsius to Fahrenheit. \n")
        for celsius, fahr in self.knownValuesCelsiusToFahr:
            print (('Testing {} conversion should be equal to {}').format(celsius, fahr))
            result = conversions.convertCelsiusToFahrenheit(celsius)
            print (('The result of the conversion: {}\n').format(result))
            self.assertEqual(fahr, result)

    def testConvertFahrenheitToCelsius(self):
        """  Tests Conversion between Fahrenheit to Celsius
        Args:
           None
        Returns:
            Assertion
        """
        print ("\nTesting conversion from Fahrenheit to Celsius. \n")
        for fahr, celsius in self.knownValuesFahrToCelsius:
            print (('Testing {} conversion should be equal to {}').format(fahr, celsius))
            result = conversions.convertFahrenheitToCelsius(fahr)
            print (('The result of the conversion: {}\n').format(result))
            self.assertEqual(celsius, result)

    def testConvertFahrenheitToKelvin(self):
        """  Tests Conversion between Fahrenheit to kelvin
        Args:
           None
        Returns:
            Assertion
        """
        print ("\nTesting conversion from Fahrenheit to Kelvin.\n")
        for fahr, kelvin in self.knownValuesFahrToKelvin:
            print ('Testing {} conversion should be equal to {}').format(fahr, kelvin)
            result = conversions.convertFahrenheitToKelvin(fahr)
            print ('The result of the conversion: {}\n').format(result)
            self.assertEqual(kelvin, result)

    def testConvertKelvinToFahrenheit(self):
        """  Tests Conversion between Kelvin to Fahrenheit
        Args:
           None
        Returns:
            Assertion
        """
        print ("\nTesting conversion from Kelvin to Fahrenheit.\n")
        for kelvin, fahr in self.knownValuesKelvinToFahr:
            print (('Testing {} conversion should be equal to {}').format(kelvin, fahr))
            result = conversions.convertKelvinToFahrenheit(kelvin)
            print (('The result of the conversion: {}\n').format(result))
            self.assertEqual(fahr, result)

    def testConvertKelvinToCelsius(self):
        """  Tests Conversion between Kelvin to Celius
        Args:
           None
        Returns:
            Assertion
        """
        print ("\nTesting conversion from Kelvin to Celsius. \n")
        for kelvin, celsius  in self.knownValuesKelvinToCels:
            print (('Testing {} convertion should be equal to {}').format(kelvin, celsius))
            result = conversions.convertKelvinToCelsius(kelvin)
            print (('The result of the conversion: {}\n').format(result))
            self.assertEqual(celsius, result)

    def testConvert(self):
        """  Tests generic unit conversion method
        Args:
           None
        Returns:
            Assertion
        """
        print ("\nTesting generic conversion method. \n")
        for fromUnit, toUnit, value, conv in self.knownValuesConvert:
            print (('Testing conversion from {} to {} with value: {}').format(fromUnit, toUnit, value))
            result = conversions_refactored.convert(fromUnit, toUnit, value)
            print (('The result of the conversion: {}\n').format(result))
            self.assertEqual(conv, result)

    def testConversionNotPossible(self):
        """  Tests to see if ConversionNotPossible is raised.
        Args:
           None
        Returns:
            Assertion
        """
        self.assertRaises(conversions_refactored.ConversionNotPossible,
                          conversions_refactored.convert('k', 'mi', 1))

if __name__ == '__main__':

    unittest.main()
