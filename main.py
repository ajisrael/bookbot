import sys

from stats import get_num_words
from stats import get_character_frequency
from stats import sort_char_freq


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    num_words = get_num_words(book_text)
    char_freq_dict = get_character_frequency(book_text)
    sorted_char_freq = sort_char_freq(char_freq_dict)

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for char_dict in sorted_char_freq:
        print(f'{char_dict["character"]}: {char_dict["count"]}')
    print('============= END ===============')

main()
