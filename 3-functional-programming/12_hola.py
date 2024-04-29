# Hola 👋🏻
# Codédex

# Define Higher Order Function
def translator(language):
  # Create a dictionary for different languages
  translations = {
    'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
    'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
    'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
  }

  def translate_word(word):
    if word.lower() in translations[language]:
      return translations[language][word.lower()]
    else:
      return 'Translation not available'

  return translate_word

# Example usage:
translate_to_spanish = translator('spanish')
print(translate_to_spanish('hello'))  # Output: hola

translate_to_french = translator('french')
print(translate_to_french('hello'))  # Output: bonjour

translate_to_italian = translator('italian')
print(translate_to_italian('hello'))  # Output: ciao

translate_to_italian = translator('italian')
print(translate_to_italian('tonight'))  # Output: Translation not available
