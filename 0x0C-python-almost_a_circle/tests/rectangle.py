import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_init(self):
        # Test the __init__ method
        rect = Rectangle(3, 4, 1, 2, 7)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 7)

    def test_width(self):
        # Test the width property and setter
        rect = Rectangle(3, 4)
        self.assertEqual(rect.width, 3)
        rect.width = 5
        self.assertEqual(rect.width, 5)
        with self.assertRaises(TypeError):
            rect.width = "invalid"
        with self.assertRaises(ValueError):
            rect.width = -1

    def test_height(self):
        # Test the height property and setter
        rect = Rectangle(3, 4)
        self.assertEqual(rect.height, 4)
        rect.height = 6
        self.assertEqual(rect.height, 6)
        with self.assertRaises(TypeError):
            rect.height = "invalid"
        with self.assertRaises(ValueError):
            rect.height = -2

    def test_x(self):
        # Test the x property and setter
        rect = Rectangle(3, 4)
        self.assertEqual(rect.x, 0)
        rect.x = 2
        self.assertEqual(rect.x, 2)
        with self.assertRaises(TypeError):
            rect.x = "invalid"
        with self.assertRaises(ValueError):
            rect.x = -3

    def test_y(self):
        # Test the y property and setter
        rect = Rectangle(3, 4)
        self.assertEqual(rect.y, 0)
        rect.y = 1
        self.assertEqual(rect.y, 1)
        with self.assertRaises(TypeError):
            rect.y = "invalid"
        with self.assertRaises(ValueError):
            rect.y = -1

    def test_area(self):
        # Test the area method
        rect = Rectangle(3, 4)
        self.assertEqual(rect.area(), 12)

    def test_display(self):
        # Test the display method
        rect = Rectangle(3, 4, 1, 2)
        expected_output = "\n\n   ###\n   ###\n   ###\n   ###\n"
        with unittest.mock.patch(
                'sys.stdout', new_callable=io.StringIO
                )
        as mock_stdout:
            rect.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        # Test the __str__ method
        rect = Rectangle(3, 4, 1, 2, 7)
        self.assertEqual(str(rect), "[Rectangle] (7) 1/2 - 3/4")

    def test_update(self):
        # Test the update method
        rect = Rectangle(3, 4, 1, 2, 7)
        rect.update(5, 6, 7, 8, 9)
        self.assertEqual(rect.id, 5)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.x, 8)
        self.assertEqual(rect.y, 9)

        rect.update(width=10, height=11, x=12, y=13)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 11)
        self.assertEqual(rect.x, 12)
        self.assertEqual(rect.y, 13)

    def test_to_dictionary(self):
        # Test the to_dictionary method
        rect = Rectangle(3, 4, 1, 2, 7)
        expected_dict = {'id': 7, 'width': 3, 'height': 4, 'x': 1, 'y': 2}
        self.assertEqual(rect.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
