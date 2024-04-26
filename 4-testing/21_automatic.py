# my_functions.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b


# test_my_functions.py
import unittest
import my_functions

class TestMyFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(my_functions.add(3, 5), 8)

    def test_multiply(self):
        self.assertEqual(my_functions.multiply(3, 4), 12)
        self.assertEqual(my_functions.multiply(2, 0), 0)

if __name__ == '__main__':
    unittest.main()
