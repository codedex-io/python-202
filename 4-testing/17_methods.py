import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        # Initialize variables for test methods
        self.test_string = "hello"
        self.expected_length = 5

    def test_string_length(self):
        # Test the length of a string
        self.assertEqual(len(self.test_string), self.expected_length)

    def test_string_contains_substring(self):
        # Test substring in a string
        substring = "ell"
        self.assertIn(substring, self.test_string)

    def test_string_uppercase(self):
        # Test string conversion to uppercase
        expected_result = "HELLO"
        self.assertEqual(self.test_string.upper(), expected_result)

if __name__ == '__main__':
    unittest.main()
