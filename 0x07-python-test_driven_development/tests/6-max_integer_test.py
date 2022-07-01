#!/usr/bin/python3
"""
unittest 6-max_integer_test
test the module 6-max_integer_test
"""


import unittest
max_integer = __import__('6-max_integer').max_integer
"""
    >>> print(max_integer([1, 2, 3, 4]))
    4
    >>> print(max_integer([1, 3, 4, 2]))
    4
    >>> print(max_integer())
    None
class TestMaxInteger(unittest.TestCase):
    def test_list(self):
        #Test the value of list
        if len(list) == 0:
            self.assertAlmostEqual(list, None)

