#!/usr/bin/python3
"""Unittest for module rectangle
"""
from models.base import Base
from models.rectangle import Rectangle
unittest = __import__("unittest")


class TestRectangleClass(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def setUp(self):
        """Reset the class-level __nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_two_params(self):
        """Test initializing with only width and height"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

    def test_four_params(self):
        """Test initializing with width, height, x, y"""
        r1 = Rectangle(2, 10, 3, 5)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 1)

    def test_five_params(self):
        """Test initializing with width, height, x, y, and id"""
        r3 = Rectangle(7, 8, 3, 4, 10)
        self.assertEqual(r3.id, 10)
        self.assertEqual(r3.width, 7)
        self.assertEqual(r3.height, 8)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)

    def test_invalid_width_type(self):
        """Test initializing with invalid width type (string instead of int)"""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_invalid_height_type(self):
        """Test initializing with invalid height type (float instead of int)"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2.5)

    def test_invalid_x_type(self):
        """Test initializing with invalid x type (float instead of int)"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 1.5, 2)

    def test_invalid_y_type(self):
        """Test initializing with invalid y type (string instead of int)"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 1, "2")

    def test_negative_width(self):
        """Test initializing with negative width"""
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)

    def test_zero_width(self):
        """Test initializing with zero width"""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_negative_height(self):
        """Test initializing with negative height"""
        with self.assertRaises(ValueError):
            Rectangle(10, -2)

    def test_zero_height(self):
        """Test initializing with zero height"""
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_negative_x(self):
        """Test initializing with negative x"""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1, 2)

    def test_negative_y(self):
        """Test initializing with negative y"""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 1, -2)

    def test_area(self):
        """Test the area calculation"""
        r4 = Rectangle(5, 4)
        self.assertEqual(r4.area(), 20)

    def test_initialization_with_negative_values(self):
        """Test initialization with negative width and height"""
        with self.assertRaises(ValueError) as context:
            r1 = Rectangle(-10, 5)
        self.assertEqual(str(context.exception), "width must be > 0")
        
        with self.assertRaises(ValueError) as context:
            r1 = Rectangle(10, -5)
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_initialization_with_zero_values(self):
        """Test initialization with zero width and height"""
        with self.assertRaises(ValueError) as context:
            r1 = Rectangle(0, 5)
        self.assertEqual(str(context.exception), "width must be > 0")
        
        with self.assertRaises(ValueError) as context:
            r1 = Rectangle(10, 0)
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_initialization_with_non_integer_values(self):
        """Test initialization with non-integer width and height"""
        with self.assertRaises(TypeError) as context:
            r1 = Rectangle(10.5, 5)
        self.assertEqual(str(context.exception), "width must be an integer")
        
        with self.assertRaises(TypeError) as context:
            r1 = Rectangle(10, "5")
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_display(self):
        """Test display method"""
        import io
        import sys
        r1 = Rectangle(4, 3)
        expected_output = "####\n####\n####\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_str_method(self):
        """Test the __str__ method output"""
        r5 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r5), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_method(self):
        """Test the update method with *args"""
        r6 = Rectangle(10, 10, 10, 10)
        r6.update(89, 4, 5, 1, 3)
        self.assertEqual(r6.id, 89)
        self.assertEqual(r6.width, 4)
        self.assertEqual(r6.height, 5)
        self.assertEqual(r6.x, 1)
        self.assertEqual(r6.y, 3)

    def test_update_kwargs(self):
        """Test the update method with **kwargs"""
        r7 = Rectangle(10, 10, 10, 10)
        r7.update(id=99, width=8, height=12, x=2, y=4)
        self.assertEqual(r7.id, 99)
        self.assertEqual(r7.width, 8)
        self.assertEqual(r7.height, 12)
        self.assertEqual(r7.x, 2)
        self.assertEqual(r7.y, 4)
