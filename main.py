import sys
from stats import get_num_words, characters, sorted_char_list


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    for char_item in sorted_char_list(characters(text)):
        if char_item["char"].isalpha():
            print(f"{char_item["char"]}: {char_item["num"]}")
    print("============= END ===============")


main()
