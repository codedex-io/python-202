import unittest

def validate_age(age):
    if not isinstance(age, int) or age <= 0:
        raise ValueError("Age must be a positive integer")
    return True

class TestValidateAgeFunction(unittest.TestCase):

    def test_invalid_negative_age(self):
        # Verify that validating a negative age raises a ValueError
        with self.assertRaises(ValueError):
            validate_age(-5)

    def test_invalid_noninteger_age(self):
        # Verify that validating a non-integer age raises a ValueError
        with self.assertRaises(ValueError):
            validate_age("twenty")

if __name__ == '__main__':
    unittest.main()

