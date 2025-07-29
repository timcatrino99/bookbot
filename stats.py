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

def sort_on(items):
    return items["num"]

def sort_char_count(chars):
    sorted_list = []
    for character in chars:
        sorted_list.append({"char": character, "num": chars[character]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list