import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_init(self):
        # Test the __init__ method
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_size(self):
        # Test the size property and setter
        square = Square(5)
        self.assertEqual(square.size, 5)
        square.size = 8
        self.assertEqual(square.size, 8)
        with self.assertRaises(TypeError):
            square.size = "invalid"
        with self.assertRaises(ValueError):
            square.size = -3

    def test_str(self):
        # Test the __str__ method
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")

    def test_update(self):
        # Test the update method
        square = Square(5, 2, 3, 1)
        square.update(6, 8, 10, 12, 14)
        self.assertEqual(square.id, 6)
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)
        self.assertEqual(square.x, 10)
        self.assertEqual(square.y, 12)

        square.update(size=15, x=18, y=20)
        self.assertEqual(square.size, 15)
        self.assertEqual(square.width, 15)
        self.assertEqual(square.height, 15)
        self.assertEqual(square.x, 18)
        self.assertEqual(square.y, 20)

    def test_to_dictionary(self):
        # Test the to_dictionary method
        square = Square(5, 2, 3, 1)
        expected_dict = {'id': 1, 'width': 5, 'height': 5, 'x': 2, 'y': 3}
        self.assertEqual(square.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
