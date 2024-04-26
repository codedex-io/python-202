import unittest

def add_numbers(a, b):
    return a + b

class TestAddition(unittest.TestCase):

    def test_adding_integers(self):
        # Test adding integers
        result = add_numbers(3, 4)
        self.assertEqual(result, 7)

    def test_adding_floats(self):
        # Test adding floating point numbers
        result = add_numbers(3.5, 4.5)
        self.assertEqual(result, 8.0)

    def test_adding_strings(self):
        # Test adding strings (should raise a TypeError)
        with self.assertRaises(TypeError):
            add_numbers("Hello", "World")

if __name__ == '__main__':
    unittest.main()
