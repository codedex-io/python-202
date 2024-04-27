# Unexpected ➗
# Codédex

import unittest
import math

def get_sqrt(n):
  return math.sqrt(n)

def divide(a, b):
  return a / b

class TestUnexpected(unittest.TestCase):

  def test_get_sqrt_valid(self):
    self.assertEqual(get_sqrt(144), 12)

  def test_get_sqrt_negative_numbers(self):
    with self.assertRaises(ValueError):
      get_sqrt(-1)

  def test_divide(self):
    self.assertEqual(divide(144, 12), 12)
  
  def test_divide_by_zero(self):
    with self.assertRaises(ZeroDivisionError):
      divide(4, 0)

if __name__ == '__main__':
  unittest.main()
