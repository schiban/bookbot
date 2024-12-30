def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words = get_count_words(text)
    count_chars = get_count_chars(text)
    sorted_list = dict_to_sorted_list(count_chars)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words} words found in the document\n")
    for char in sorted_list:
        print(f"The '{char['char']}' character was found {char['times']} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_count_words(text):
    words = text.split()
    return len(words)


def get_count_chars(text):
    chars = {}
    for char in text.lower():
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars


def sort_on(dict):
    return dict["times"]


def dict_to_sorted_list(chars):
    list_chars = []
    for char in chars:
        list_chars.append({"char": char, "times": chars[char]})
    list_chars.sort(reverse=True, key=sort_on)
    return list_chars

main()