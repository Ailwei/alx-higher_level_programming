import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_to_json_string(self):
        # Test the to_json_string method
        obj = Rectangle(1, 2, 3, 4, 5)
        result = Base.to_json_string([obj.to_dictionary()])
        expected = '[{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]'
        self.assertEqual(result, expected)

    def test_save_to_file(self):
        # Test the save_to_file method
        obj = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([obj])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}]')
        os.remove("Rectangle.json")

    def test_create(self):
        # Test the create method
        obj_dict = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        obj = Base.create(**obj_dict)
        self.assertIsInstance(obj, Rectangle)
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 3)
        self.assertEqual(obj.x, 4)
        self.assertEqual(obj.y, 5)

    def test_load_from_file(self):
        # Test the load_from_file method
        obj = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([obj])
        loaded_objs = Rectangle.load_from_file()
        self.assertEqual(len(loaded_objs), 1)
        loaded_obj = loaded_objs[0]
        self.assertIsInstance(loaded_obj, Rectangle)
        self.assertEqual(loaded_obj.id, 5)
        self.assertEqual(loaded_obj.width, 1)
        self.assertEqual(loaded_obj.height, 2)
        self.assertEqual(loaded_obj.x, 3)
        self.assertEqual(loaded_obj.y, 4)
        os.remove("Rectangle.json")

    def test_to_csv_row(self):
        # Test the to_csv_row method
        obj = Rectangle(1, 2, 3, 4, 5)
        row = Base.to_csv_row(obj.to_dictionary())
        expected = ["5", "1", "2", "3", "4"]
        self.assertEqual(row, expected)

    def test_from_csv_row(self):
        # Test the from_csv_row method
        row = ["5", "1", "2", "3", "4"]
        obj_dict = Base.from_csv_row(row)
        expected = {"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}
        self.assertEqual(obj_dict, expected)

    def test_save_to_file_csv(self):
        # Test the save_to_file_csv method
        obj = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file_csv([obj])
        with open("Rectangle.csv", "r") as file:
            content = file.read()
            self.assertEqual(content, "5,1,2,3,4\n")
        os.remove("Rectangle.csv")

    def test_load_from_file_csv(self):
        # Test the load_from_file_csv method
        obj = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file_csv([obj])
        loaded_objs = Rectangle.load_from_file_csv()
        self.assertEqual(len(loaded_objs), 1)
        loaded_obj = loaded_objs[0]
        self.assertIsInstance(loaded_obj, Rectangle)
        self.assertEqual(loaded_obj.id, 5)
        self.assertEqual(loaded_obj.width, 1)
        self.assertEqual(loaded_obj.height, 2)
        self.assertEqual(loaded_obj.x, 3)
        self.assertEqual(loaded_obj.y, 4)
        os.remove("Rectangle.csv")


if __name__ == '__main__':
    unittest.main()
