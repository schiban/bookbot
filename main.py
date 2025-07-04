from stats import get_book_text
from stats import get_count_words
from stats import get_count_chars
from stats import dict_to_sorted_list
import sys

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    count_words = get_count_words(text)
    count_chars = get_count_chars(text)
    sorted_list = dict_to_sorted_list(count_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words} total words")
    print("--------- Character Count -------")
    for char in sorted_list:
        print(f"{char['char']}: {char['times']}")
    print("============= END ===============")

main()