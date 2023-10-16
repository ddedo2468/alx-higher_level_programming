#!/usr/bin/python3
""" defines unittest for Rectangle """
import unittest
import io
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init(self):
        r1 = Rectangle(10, 7)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 7)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 4, 1, 9, 100)
        self.assertEqual(r2.id, 100)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 9)

    def test_area(self):
        r1 = Rectangle(10, 7)
        self.assertEqual(r1.area(), 70)

        r2 = Rectangle(2, 4, 1, 9, 100)
        self.assertEqual(r2.area(), 8)

    def test_display(self):
        r1 = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r1.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        r2 = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r2.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/8 - 10/7")

        r2 = Rectangle(2, 4, 1, 9, 100)
        self.assertEqual(str(r2), "[Rectangle] (100) 1/9 - 2/4")

    def test_update(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 2/8 - 10/7")

        r2 = Rectangle(2, 4, 1, 9, 100)
        r2.update(89, 2)
        self.assertEqual(str(r2), "[Rectangle] (89) 1/9 - 2/4")

    def test_to_dictionary(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r1_dict = r1.to_dictionary()
        expected_dict = {'id': 1, 'width': 10, 'height': 7, 'x': 2, 'y': 8}
        self.assertEqual(r1_dict, expected_dict)

        r2 = Rectangle(2, 4, 1, 9, 100)
        r2_dict = r2.to_dictionary()
        expected_dict = {'id': 100, 'width': 2, 'height': 4, 'x': 1, 'y': 9}
        self.assertEqual(r2_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
