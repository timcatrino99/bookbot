def book_word_count(text):
    words = text.split()
    return len(words)

def book_char_count(text):
    text_lower = text.lower()
    chars = {}

    for char in text_lower:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    
    return chars