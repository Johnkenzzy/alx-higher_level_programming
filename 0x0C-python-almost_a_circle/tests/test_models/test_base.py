#!/usr/bin/python3
"""Unittest for module base
Checks for diferrent test cases
"""
from models.base import Base
unittest = __import__("unittest")


class TestBaseClass(unittest.TestCase):
    """Test cases for the Base class definition"""

    def setUp(self):
        """Reset the class-level __nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_id_notprovided(self):
        """Test not providing an id during initialization"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id_provided(self):
        """Test that providing an id during initialization works correctly"""
        b1 = Base(7)
        self.assertEqual(b1.id, 7)

    def test_id_auto_increment(self):
        """Test that ids are auto-incremented if not provided"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_mixed(self):
        """Test a mix of provided ids and auto-incremented ids"""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)

    def test_id_multiple_instances(self):
        """Test that multiple instances correctly maintain unique ids"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
