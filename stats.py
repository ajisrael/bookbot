def get_num_words(book_text):
    return len(book_text.split())


def get_character_frequency(book_text):
    lowercase_text = book_text.lower()
    char_freq_dict = {}

    for char in lowercase_text:
        char_freq_dict[char] = char_freq_dict.setdefault(char, 0) + 1

    return char_freq_dict


def sort_on(dict):
    return dict["count"]


def sort_char_freq(char_freq_dict):
    frequencies = []

    for key in char_freq_dict:
        frequencies.append({"character": key, "count": char_freq_dict[key]})

    frequencies.sort(key=sort_on, reverse=True)
    return frequencies
