import unittest

def add_numbers(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    # Define the first Unit Test
    def test_addition(self):
        # Define variables
        num1 = 3
        num2 = 4

        # Define the test
        result = add_numbers(num1, num2)

        # Define the expected result
        expected_result = 7
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
