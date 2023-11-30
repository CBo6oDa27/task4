def make_upper_word(word):
    """Возвращает слово заглавными буквами"""
    return  word.upper()

def capitalize_words(words):
    """Изменяет первые буквы слов на заглавные"""
    capitalized_words = ' '.join(word.capitalize() for word in words.split())
    return capitalized_words