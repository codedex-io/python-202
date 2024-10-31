# Assertions 🧵
# Codédex

import unittest
from string_utils import reverse_string, capitalize_string, is_capitalized

class TestStringUtils(unittest.TestCase):

  def test_reverse_string(self):
    # Test cases for reversing a string
    self.assertEqual(reverse_string('mochi'), 'ihcom')
    self.assertEqual(reverse_string('hello'), 'olleh')
    self.assertEqual(reverse_string('Python'), 'nohtyP')
    self.assertEqual(reverse_string(''), '')  # Empty string case

  def test_capitalize_string(self):
    # Test cases for capitalizing a string
    self.assertEqual(capitalize_string('mochi'), 'Mochi')
    self.assertEqual(capitalize_string('hello'), 'Hello')
    self.assertEqual(capitalize_string('python'), 'Python')
    self.assertEqual(capitalize_string('hELLO'), 'Hello')  # Should fix mixed case
    self.assertEqual(capitalize_string(''), '')  # Empty string case

  def test_is_capitalized(self):
    # Test cases for checking if the string is capitalized
    self.assertTrue(is_capitalized('Mochi'))
    self.assertFalse(is_capitalized('mochi'))  # This case should return False
    self.assertTrue(is_capitalized('Hello'))
    self.assertFalse(is_capitalized('hello'))
    self.assertFalse(is_capitalized(''))  # Empty string should return False

if __name__ == '__main__':
  unittest.main()
