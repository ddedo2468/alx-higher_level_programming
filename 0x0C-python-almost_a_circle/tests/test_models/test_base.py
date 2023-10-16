#!/usr/bin/python3
""" defines unittests for Base """
import unittest
import os
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_base_constructor(self):
        base = Base()
        self.assertEqual(base.id, 1)
        base2 = Base()
        self.assertEqual(base2.id, 2)

    def test_base_constructor_with_id(self):
        base = Base(50)
        self.assertEqual(base.id, 50)
        base2 = Base(100)
        self.assertEqual(base2.id, 100)

    def test_base_to_json_string_empty(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_base_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        dict_list = [r1.to_dictionary(), r2.to_dictionary()]
        json_string = Base.to_json_string(dict_list)
        self.assertEqual(json_string, json.dumps(dict_list))

    def test_base_to_json_string_none(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_base_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Base.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            data = json.load(file)
        expected_data = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertEqual(data, expected_data)
        os.remove("Rectangle.json")

    def test_base_save_to_file_empty_list(self):
        Base.save_to_file([])
        with open("Rectangle.json", "r") as file:
            data = json.load(file)
        self.assertEqual(data, [])
        os.remove("Rectangle.json")

    def test_base_save_to_file_none(self):
        Base.save_to_file(None)
        self.assertFalse(os.path.exists("Rectangle.json"))

    def test_base_from_json_string_empty(self):
        json_string = "[]"
        data = Base.from_json_string(json_string)
        self.assertEqual(data, [])

    def test_base_from_json_string(self):
        data = [
            {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8},
            {'id': 2, 'width': 2, 'height': 4, 'x': 0, 'y': 0}
        ]
        json_string = json.dumps(data)
        returned_data = Base.from_json_string(json_string)
        self.assertEqual(returned_data, data)

    def test_base_create(self):
        r = Rectangle(2, 4)
        r_dict = r.to_dictionary()
        new_r = Rectangle.create(**r_dict)
        self.assertIsNot(r, new_r)
        self.assertNotEqual(r, new_r)
        self.assertEqual(r.to_dictionary(), new_r.to_dictionary())

    def test_base_load_from_file(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        data = [
            {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8},
            {'id': 2, 'width': 2, 'height': 4, 'x': 0, 'y': 0}
        ]
        json_string = json.dumps(data)
        with open("Rectangle.json", "w") as file:
            file.write(json_string)

        rectangles = Rectangle.load_from_file()
        self.assertIsInstance(rectangles, list)
        self.assertTrue(all(isinstance(r, Rectangle) for r in rectangles))
        self.assertEqual(len(rectangles), 2)
        self.assertEqual(rectangles[0].to_dictionary(), data[0])
        self.assertEqual(rectangles[1].to_dictionary(), data[1])

    def test_base_load_from_file_empty(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        rectangles = Rectangle.load_from_file()
        self.assertIsInstance(rectangles, list)
        self.assertEqual(len(rectangles), 0)


if __name__ == '__main__':
    unittest.main()
