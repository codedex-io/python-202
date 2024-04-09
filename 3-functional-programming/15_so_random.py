# So Random 🌙
# Codédex

import random

# Lists of prefixes and suffixes for fantasy names
prefixes = ['Dark', 'Hope', 'Moon', 'Golden', 'Silver']
suffixes = ['river', 'fire', 'storm', 'whisper', 'song']

# Generate fantasy names using list comprehension
fantasy_names = [prefix + ' ' + suffix for prefix in prefixes for suffix in suffixes]

# Shuffle the generated fantasy names for randomness
random.shuffle(fantasy_names)

# Display the generated fantasy names
print('Fantasy User Names:')
for name in fantasy_names:
  print(name)
