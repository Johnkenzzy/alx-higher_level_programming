#!/usr/bin/python3
"""Unittest for module rectangle
"""
from models.rectangle import Rectangle
unittest = __import__("unittest")


class TestRectangle(unittest.TestCase):
    def setUp(self):
        """Set up a Rectangle instance for testing."""
        self.rectangle = Rectangle(4, 6, 2, 3, 1)

    def test_initialization(self):
        """Test the initialization of the Rectangle."""
        self.assertEqual(self.rectangle.width, 4)
        self.assertEqual(self.rectangle.height, 6)
        self.assertEqual(self.rectangle.x, 2)
        self.assertEqual(self.rectangle.y, 3)
        self.assertEqual(self.rectangle.id, 1)

    def test_area(self):
        """Test the area calculation of the Rectangle."""
        self.assertEqual(self.rectangle.area(), 24)  # 4 * 6

    def test_display(self):
        """Test the display method."""
        expected_output = "\n\n###\n###\n###\n###\n###\n###\n"
        with unittest.mock.patch('sys.stdout', new_callable=unittest.mock.StringIO) as mock_stdout:
            self.rectangle.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_string_representation(self):
        """Test the string representation of the Rectangle."""
        expected = "[Rectangle] (1) 2/3 - 4/6"
        self.assertEqual(str(self.rectangle), expected)

    def test_width_getter(self):
        """Test the width getter."""
        self.assertEqual(self.rectangle.width, 4)

    def test_width_setter(self):
        """Test the width setter with valid value."""
        self.rectangle.width = 5
        self.assertEqual(self.rectangle.width, 5)

    def test_width_setter_invalid_type(self):
        """Test width setter with invalid type."""
        with self.assertRaises(TypeError):
            self.rectangle.width = "not an integer"

    def test_width_setter_invalid_value(self):
        """Test width setter with invalid value."""
        with self.assertRaises(ValueError):
            self.rectangle.width = 0
        with self.assertRaises(ValueError):
            self.rectangle.width = -1

    def test_height_getter(self):
        """Test the height getter."""
        self.assertEqual(self.rectangle.height, 6)

    def test_height_setter(self):
        """Test the height setter with valid value."""
        self.rectangle.height = 10
        self.assertEqual(self.rectangle.height, 10)

    def test_height_setter_invalid_type(self):
        """Test height setter with invalid type."""
        with self.assertRaises(TypeError):
            self.rectangle.height = "not an integer"

    def test_height_setter_invalid_value(self):
        """Test height setter with invalid value."""
        with self.assertRaises(ValueError):
            self.rectangle.height = 0
        with self.assertRaises(ValueError):
            self.rectangle.height = -1

    def test_x_getter(self):
        """Test the x getter."""
        self.assertEqual(self.rectangle.x, 2)

    def test_x_setter(self):
        """Test the x setter with valid value."""
        self.rectangle.x = 5
        self.assertEqual(self.rectangle.x, 5)

    def test_x_setter_invalid_type(self):
        """Test x setter with invalid type."""
        with self.assertRaises(TypeError):
            self.rectangle.x = "not an integer"

    def test_x_setter_invalid_value(self):
        """Test x setter with invalid value."""
        with self.assertRaises(ValueError):
            self.rectangle.x = -1

    def test_y_getter(self):
        """Test the y getter."""
        self.assertEqual(self.rectangle.y, 3)

    def test_y_setter(self):
        """Test the y setter with valid value."""
        self.rectangle.y = 4
        self.assertEqual(self.rectangle.y, 4)

    def test_y_setter_invalid_type(self):
        """Test y setter with invalid type."""
        with self.assertRaises(TypeError):
            self.rectangle.y = "not an integer"

    def test_y_setter_invalid_value(self):
        """Test y setter with invalid value."""
        with self.assertRaises(ValueError):
            self.rectangle.y = -1

    def test_update_with_args(self):
        """Test the update method with positional arguments."""
        self.rectangle.update(2, 5, 7, 1, 3)
        self.assertEqual(self.rectangle.id, 2)
        self.assertEqual(self.rectangle.width, 5)
        self.assertEqual(self.rectangle.height, 7)
        self.assertEqual(self.rectangle.x, 1)
        self.assertEqual(self.rectangle.y, 3)

    def test_update_with_kwargs(self):
        """Test the update method with keyword arguments."""
        self.rectangle.update(width=10, x=5)
        self.assertEqual(self.rectangle.width, 10)
        self.assertEqual(self.rectangle.x, 5)
        self.assertEqual(self.rectangle.height, 6)  # Should remain unchanged

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        expected_dict = {
            'id': 1,
            'width': 4,
            'height': 6,
            'x': 2,
            'y': 3
        }
        self.assertEqual(self.rectangle.to_dictionary(), expected_dict)

    def tearDown(self):
        """Clean up after tests."""
        del self.rectangle
