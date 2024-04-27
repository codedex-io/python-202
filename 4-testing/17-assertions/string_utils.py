# Assertions 🧵
# Codédex

def reverse_string(s):
  return s[::-1]

def capitalize_string(s):
  return s.capitalize()

def has_capital_letters(s):
  for char in s:
    if char.isupper():
      return True
  return False