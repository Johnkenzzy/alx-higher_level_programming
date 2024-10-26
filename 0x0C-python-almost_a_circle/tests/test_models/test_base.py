#!/usr/bin/python3
"""Unittest for module base

Supplies the test classes:
    TestBaseClass
    TestBaseToJsonString
    TestBaseSaveToFile
    TestBaseFromJsonString
    TestBaseCreate
    TestBaseLoadFromFile
    TestBaseCSV
"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
import csv
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

    def test_id_zero(self):
        """Test that an id of zero is correctly assigned"""
        b1 = Base(0)
        self.assertEqual(b1.id, 0)

    def test_id_negative(self):
        """Test that a negative id is correctly assigned"""
        b1 = Base(-5)
        self.assertEqual(b1.id, -5)

    def test_id_non_integer(self):
        """Test assigning a non-integer id"""
        b1 = Base("Test")
        self.assertEqual(b1.id, "Test")


class TestBaseToJsonString(unittest.TestCase):
    """Test cases for the to_json_string method"""

    def test_to_json_string_empty_list(self):
        """Test passing an empty list"""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        """Test passing None"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_valid_list(self):
        """Test passing a valid list of dictionaries"""
        dicts = [{"id": 1, "width": 10, "height": 4}, {"id": 2, "size": 5}]
        json_str = Base.to_json_string(dicts)
        string = '[{"id": 1, "width": 10, "height": 4}, {"id": 2, "size": 5}]'
        self.assertEqual(json_str, string)

    def test_to_json_string_empty_dict(self):
        """Test passing a list containing an empty dictionary"""
        self.assertEqual(Base.to_json_string([{}]), "[{}]")


class TestBaseSaveToFile(unittest.TestCase):
    """Test cases for the save_to_file method"""

    def setUp(self):
        """Ensure no leftover files before starting the test"""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """Clean up files created during tests"""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    def test_save_to_file_none(self):
        """Test saving None to a file"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty_list(self):
        """Test saving an empty list to a file"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_valid_objects(self):
        """Test saving a list of Rectangle objects to a file"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r", encoding="utf-8") as file:
            self.assertTrue(len(file.read()) > 0)


class TestBaseFromJsonString(unittest.TestCase):
    """Test cases for the from_json_string method"""

    def test_from_json_string_none(self):
        """Test passing None"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test passing an empty string"""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_valid(self):
        """Test passing a valid JSON string"""
        json_str = '[{"id": 1, "width": 10}, {"id": 2, "size": 5}]'
        dicts = Base.from_json_string(json_str)
        self.assertEqual(dicts, [{"id": 1, "width": 10}, {"id": 2, "size": 5}])

    def test_from_json_string_empty_dict(self):
        """Test passing a JSON string of an empty dictionary"""
        self.assertEqual(Base.from_json_string("[{}]"), [{}])


class TestBaseFromJsonString(unittest.TestCase):
    """Test cases for the from_json_string method"""

    def test_from_json_string_none(self):
        """Test passing None"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test passing an empty string"""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_valid(self):
        """Test passing a valid JSON string"""
        json_str = '[{"id": 1, "width": 10}, {"id": 2, "size": 5}]'
        dicts = Base.from_json_string(json_str)
        self.assertEqual(dicts, [{"id": 1, "width": 10}, {"id": 2, "size": 5}])

    def test_from_json_string_empty_dict(self):
        """Test passing a JSON string of an empty dictionary"""
        self.assertEqual(Base.from_json_string("[{}]"), [{}])


class TestBaseCreate(unittest.TestCase):
    """Test cases for the create method"""

    def test_create_rectangle(self):
        """Test creating a Rectangle instance from a dictionary"""
        dictionary = {"id": 89, "width": 10, "height": 4, "x": 1, "y": 2}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 2)

    def test_create_square(self):
        """Test creating a Square instance from a dictionary"""
        dictionary = {"id": 89, "size": 4, "x": 1, "y": 2}
        s1 = Square.create(**dictionary)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 2)


class TestBaseLoadFromFile(unittest.TestCase):
    """Test cases for the load_from_file method"""

    def setUp(self):
        """Ensure no leftover files before starting the test"""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """Clean up files created during tests"""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    def test_load_from_file_no_file(self):
        """Test loading from a file that doesn't exist"""
        rectangles = Rectangle.load_from_file()
        self.assertEqual(rectangles, [])

    def test_load_from_file_valid(self):
        """Test loading objects from a valid file"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)
        self.assertEqual(rectangles[0].id, 1)
        self.assertEqual(rectangles[1].id, 2)


class TestBaseCSV(unittest.TestCase):
    """Test cases for save_to_file_csv and load_from_file_csv methods"""

    def setUp(self):
        """Ensure no leftover files before starting the test"""
        try:
            os.remove("Rectangle.csv")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.csv")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """Clean up files created during tests"""
        try:
            os.remove("Rectangle.csv")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.csv")
        except FileNotFoundError:
            pass

    def test_save_to_file_csv_empty_list(self):
        """Test saving an empty list to a CSV file"""
        Rectangle.save_to_file_csv([])
        with open("Rectangle.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            rows = list(reader)
            self.assertEqual(len(rows), 0)

    def test_save_load_file_csv_rectangle(self):
        """Test saving and loading a list of Rectangle objects from CSV file"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        rectangles = Rectangle.load_from_file_csv()
        self.assertEqual(len(rectangles), 2)
        self.assertEqual(rectangles[0].width, 10)
        self.assertEqual(rectangles[1].height, 4)

    def test_save_load_file_csv_square(self):
        """Test saving and loading a list of Square objects from a CSV file"""
        s1 = Square(5, 1, 2, 3)
        s2 = Square(7, 3, 4, 5)
        Square.save_to_file_csv([s1, s2])
        squares = Square.load_from_file_csv()
        self.assertEqual(len(squares), 2)
        self.assertEqual(squares[0].size, 5)
        self.assertEqual(squares[1].size, 7)
