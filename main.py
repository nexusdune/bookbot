from stats import get_num_words, get_chars_dict, sort_on
import sys


def main():
    if (len(sys.argv)) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_dict = sort_on(chars_dict)
    print(f"Found {num_words} total words")
    # print("---------- Found  -------")
    # print(chars_dict)
    # print("------ Found characters (sorted) -------")
    # print(sorted_dict)
    for ch in sorted_dict:
        print(f"{ch["char"]}: {ch["num"]} ")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
