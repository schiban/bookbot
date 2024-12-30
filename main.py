def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words = get_count_words(text)
    count_chars = get_count_chars(text)
    print(count_chars)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_count_words(text):
    words = text.split()
    return len(words)


def get_count_chars(text):
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


main()