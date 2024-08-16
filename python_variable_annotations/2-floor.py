#!/usr/bin/env python3
"""
A simple module for mathematical operations.

This module includes a function that utilizes the `math` library to
calculate the floor of a floating-point number.
"""

import math


def floor(n: float) -> int:
    """
    Return the floor of a floating-point number.

    The floor of a number is the largest integer less than or equal to the given number.
    
    Args:
        n (float): The floating-point number to be floored.

    Returns:
        int: The floor of the given number.
    
    Example:
        >>> floor(3.7)
        3
        >>> floor(-2.3)
        -3
    """
    return math.floor(n)