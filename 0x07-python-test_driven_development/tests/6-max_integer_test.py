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
        self.assertEqual(max_integer([0.24, 0.57, 0.03, 0.78]), 0.78)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([7]), 7)
        self.assertEqual(max_integer([float('-inf'), float('inf')]), float('inf'))
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([-1, 0, 1]), 1)
        self.assertEqual(max_integer([3.5, 2.7, 3.8, 2.9]), 3.8)
        self.assertEqual(max_integer([2**32, -2**32, 2**16, -2**16]), 2**32)
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')
        self.assertEqual(max_integer(["apple", "banana", "pear"]), "pear")
