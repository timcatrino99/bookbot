from stats import book_word_count
from stats import book_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = book_word_count(book)
    print(f"{num_words} words found in the document")
    num_chars = book_char_count(book)
    print(num_chars)

main()