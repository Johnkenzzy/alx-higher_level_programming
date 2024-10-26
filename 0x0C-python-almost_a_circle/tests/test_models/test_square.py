#!/usr/bin/python3
"""Unittest for module rectangle
"""
from models.square import Square
from models.rectangle import Rectangle
unittest = __import__("unittest")


class TestSquare(unittest.TestCase):
    def setUp(self):
        """Set up a Square instance for testing"""
        self.square = Square(5, 2, 3, 1)

    def test_initialization(self):
        """Test the initialization of the Square"""
        self.assertEqual(self.square.size, 5)
        self.assertEqual(self.square.x, 2)
        self.assertEqual(self.square.y, 3)
        self.assertEqual(self.square.id, 1)

    def test_string_representation(self):
        """Test the string representation of the Square"""
        expected = "[Square] (1) 2/3 - 5"
        self.assertEqual(str(self.square), expected)

    def test_size_getter(self):
        """Test the size getter"""
        self.assertEqual(self.square.size, 5)

    def test_size_setter(self):
        """Test the size setter with valid value"""
        self.square.size = 10
        self.assertEqual(self.square.size, 10)

    def test_size_setter_invalid_type(self):
        """Test size setter with invalid type"""
        with self.assertRaises(TypeError):
            self.square.size = "not an integer"

    def test_size_setter_invalid_value(self):
        """Test size setter with invalid value"""
        with self.assertRaises(ValueError):
            self.square.size = 0
        with self.assertRaises(ValueError):
            self.square.size = -1

    def test_update_with_args(self):
        """Test the update method with positional arguments"""
        self.square.update(2, 10, 1, 0)
        self.assertEqual(self.square.id, 2)
        self.assertEqual(self.square.size, 10)
        self.assertEqual(self.square.x, 1)
        self.assertEqual(self.square.y, 0)

    def test_update_with_kwargs(self):
        """Test the update method with keyword arguments"""
        self.square.update(size=20, x=3)
        self.assertEqual(self.square.size, 20)
        self.assertEqual(self.square.x, 3)
        self.assertEqual(self.square.y, 3)

    def test_to_dictionary(self):
        """Test the to_dictionary method"""
        expected_dict = {'id': 1, 'x': 2, 'size': 5, 'y': 3}
        self.assertEqual(self.square.to_dictionary(), expected_dict)

    def test_square_inheritance(self):
        """Test that Square is a subclass of Rectangle"""
        self.assertIsInstance(self.square, Rectangle)

    def test_default_square_size(self):
        """Test initialization of Square with default parameters"""
        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def tearDown(self):
        """Clean up after tests"""
        del self.square

    def test_update_with_partial_args(self):
        """Test update method with partial positional arguments"""
        self.square.update(42, 7)
        self.assertEqual(self.square.id, 42)
        self.assertEqual(self.square.size, 7)
        self.assertEqual(self.square.x, 2)
        self.assertEqual(self.square.y, 3)

    def test_update_with_partial_kwargs(self):
        """Test update method with partial keyword arguments"""
        self.square.update(size=15)
        self.assertEqual(self.square.size, 15)
        self.assertEqual(self.square.id, 1)
        self.assertEqual(self.square.x, 2)
        self.assertEqual(self.square.y, 3)

    def test_invalid_x_y_values(self):
        """Test setting invalid x and y values"""
        with self.assertRaises(ValueError):
            self.square.x = -1
        with self.assertRaises(ValueError):
            self.square.y = -2
