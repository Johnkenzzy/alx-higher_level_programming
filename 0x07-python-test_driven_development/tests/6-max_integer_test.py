#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test class for max_integer function test suit"""

    def test_maxint(self):
        self.assertEqual(max_integer([1, 4, 10, 2]), 10)
        self.assertEqual(max_integer([1, 4, -10, 2]), 4)
        self.assertEqual(max_integer([-1, -4, -10, -2]), -1)
        self.assertEqual(max_integer([1.16, 2.98, 2.76, 2.34]), 2.98)
        self.assertEqual(max_integer([5 * 9, 4, 1000 / 10, 2]), 100)
        self.assertEqual(max_integer([1, 4, -0, 2]), 4)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([1, 4, 10, 2]), 10)
        self.assertEqual(max_integer([]), None)

