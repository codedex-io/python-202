# Caffeinated ☕️
# Codédex

import unittest
from coffee_menu import CoffeeMenu

class TestCoffeeMenu(unittest.TestCase):

  def setUp(self):
    self.menu = CoffeeMenu()

  def test_get_price_existing_item(self):
    self.assertEqual(self.menu.get_price('latte'), 3.00)

  def test_get_price_non_existing_item(self):
    self.assertIsNone(self.menu.get_price('mocha'))

  def test_add_item(self):
    self.menu.add_item('mocha', 3.50)
    self.assertEqual(self.menu.get_price('mocha'), 3.50)

if __name__ == '__main__':
  unittest.main()