#!/usr/bin/env python

"""
Author: Nick Russo
File: triangle.py
Purpose: Defines a Triangle object, inherited from the abstract class Shape.
"""

from math import sqrt
from shapes.shape import Shape


class Triangle(Shape):
    """
    Represents a Triangle shape, and contains a value for each of the three sides, side_a, side_b,
    and side_c.
    """

    decimal_places = 2
    
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        """
        Compute the area using Heron's Formula. 
        Step 1: Calulate _s.  _s = (side_a + side_b + side_c) /2
        Step 2: Area = sqrt(s * (_s - side_a) * (_s - side_b) * (_s - side_c))
        """
        perim_2 = (self.side_a + self.side_b + self.side_c) / 2
        
        return round (sqrt (perim_2 - self.side_a) * (perim_2 - self.side_b) * (perim_2 - self.side_c), self.decimal_places)

    def perimeter(self):
        """
        Compute the perimeter using the formula side_a + side_b + side_c
        """
        return self.side_a + self.side_b + self.side_c

