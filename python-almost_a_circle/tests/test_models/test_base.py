#!/usr/bin/python3
"""Test unittest for class Base"""
import unittest
import pycodestyle
from models.base import Base


class TestInit(unittest.TestCase):
    """class test for id"""

    def test_base_instanciation(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(73)
        self.assertEqual(b3.id, 73)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_id_is_str(self):
        """Test with string"""
        b1 = Base("Test")
        self.assertEqual(b1.id, "Test")


class test_to_json_string(unittest.TestCase):
    """class test for methode to_json_string"""

    def test_to_json_string_empty_list(self):
        """Test with an empty list of objects"""
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")


class TestPEP8(unittest.TestCase):
    def test_pep8_conformance(self):
        style = pycodestyle.StyleGuide()
        result = style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0, "PEP 8 violations found")


if __name__ == '__main__':
    unittest.main()
