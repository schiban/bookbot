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