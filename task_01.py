#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This function coverts temperature in different standards"""

import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """Convert the degrees Fahrenheit to a decimal representation of degrees
       Celsius

    Args:
        degrees (int): Temperature in degree Fahrenheit
    Returns:
        decimal.Decimal: Temperature in degree Celsius
    Example:

        >>> fahrenheit_to_celsius(95)
        35
    """
    DEGREE = decimal.Decimal('{}'.format(degrees))
    return decimal.Decimal('{}'.format((DEGREE - 32) * 5 / 9))


def celsius_to_kelvin(degrees):
    """Convert the degrees Celsius to Kelvin

    Args:
        degrees (decimal.Decimal): Temperature in degree Celsius
    Returns:
        decimal.Decimal: Temperature in degree Kelvin
    Example:

        >>> print celsius_to_kelvin(20)
        293.15
    """
    return decimal.Decimal('{}'.format(degrees + ABSOLUTE_DIFFERENCE))


def fahrenheit_to_kelvin(degrees):
    """Convert the degrees Fahrenheit to Kelvin

    Args:
        degrees (decimal.Decimal): Temperature in degree Fahrenheit
    Returns:
        decimal.Decimal: Temperature in degree Kelvin
    Example:

        >>> fahrenheit_to_kelvin(95)
        308.15
    """
    return celsius_to_kelvin(fahrenheit_to_celsius(degrees))
