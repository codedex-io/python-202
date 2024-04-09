# Define Higher Order Function
def translator(language):
    # Create a dictionary for different languages
    translations = {
        'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
        'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
        'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
    }

    def translate_word(word):
        return translations[language].get(word.lower(), "Translation not available")

    return translate_word

# Example usage:
translate_to_spanish = translator('spanish')
print(translate_to_spanish('hello'))  # Output: hola

translate_to_french = translator('french')
print(translate_to_french('hello'))  # Output: au revoir

translate_to_italian = translator('italian')
print(translate_to_italian('hello'))  # Output: grazie

translate_to_italian = translator('italian')
print(translate_to_italian('tonight'))  # Output: Translation not available
