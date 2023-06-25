import re
import string


def capitalize_first(string):
    return string.capitalize()


def snake_case(string):
    words = re.findall(r'[A-Za-z0-9]+', string)
    return '_'.join(words).lower()


def camel_case(string):
    words = re.findall(r'[A-Za-z0-9]+', string)
    return ''.join(word.capitalize() for word in words)


def count_occurrences(string, substring):
    return string.count(substring)


def replace_first(string, old_substring, new_substring):
    return string.replace(old_substring, new_substring, 1)


def replace_all(string, old_substring, new_substring):
    return string.replace(old_substring, new_substring)


def split_by_space(string):
    return string.split()


def split_by_character(string, character):
    return string.split(character)


def join_with_space(strings):
    return ' '.join(strings)


def join_with_character(strings, character):
    return character.join(strings)


def to_uppercase(string):
    return string.upper()


def to_lowercase(string):
    return string.lower()


def remove_whitespace(string):
    return ''.join(string.split())


def trim(string):
    return string.strip()


def remove_punctuation(string):
    translator = str.maketrans('', '', string.punctuation)
    return string.translate(translator)


def is_palindrome(string):
    cleaned_string = remove_punctuation(string.lower())
    return cleaned_string == cleaned_string[::-1]


def count_characters(string, character):
    return string.count(character)


def is_substring_available(string, substring):
    return substring in string


def count_substring_occurrences(string, substring):
    return string.count(substring)


def lower_bound(string, substring):
    return string.index(substring) if substring in string else -1


def upper_bound(string, substring):
    return string.rindex(substring) if substring in string else -1


def get_length(string):
    return len(string)


def get_word_extracted(string, index):
    words = re.findall(r'[A-Za-z0-9]+', string)
    return words[index] if 0 <= index < len(words) else ''


def is_alphanumeric(string):
    return string.isalnum()


def is_numeric(string):
    return string.isnumeric()


def get_frequency(string):
    frequencies = {}
    for char in string:
        frequencies[char] = frequencies.get(char, 0) + 1
    return frequencies


def reverse_text(string):
    return string[::-1]


def sub_string_conversion(string, substring, new_case):
    return string.replace(substring, new_case)


# Additional functions for alphabet 'N'
def get_alphabet_n():
    return 'N'


def alphabet_n_occurrences(string):
    return string.count(get_alphabet_n())
