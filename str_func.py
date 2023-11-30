def make_upper_word(word):
    """Возвращает слово заглавными буквами из PyCharm"""
    return  word.upper()

def capitalize_word(word):
    """Возвращает слова с первыми заглавными буквами"""
    capitalized_words = ' '.join(word.capitalize() for word in word.split())
    return capitalized_words
