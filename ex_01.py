"""
Universität Tübingen - Seminar für Sprachwissenschaft
VL 'Programming and Data Analysis' SS 2019
© Johannes Dellert, Maxim Korniyenko, Natalie Clarius, Gerhard Jäger

Assignment 01: Transliteration
Template
"""


def am_to_br(word):
    """
    Transliterate an American word with "or" (like "color" in American English) into its British English variant with
     "our" ("colour") instead.
    :param word: the AE word to be converted to BE
    :type word: str
    :return: the BE transliteration of word
    :rtype: str
    """
    word = word.replace("or", "our")
    return word


def diddle_latin(word):
    """
    Transliterate a word into its diddle latin variant.
    In diddle latin, each word is prefixed with "diddl", and the first letter of the word is moved to the end of the
    word.
    :param word: the word to be diddle-latinized
    :type word: str
    :return: the diddle latin transliteration of word
    :rtype: str
    """
    word = "diddl" + word[1:] + word[0]
    return word


def diddle_latin_name(word):
    """
    Transliterate a word into its diddle latin variant, paying attention to uppercase letters.
    :param word: the word to be diddle-latinized with attention to case
    :type word: str
    :return: the diddle latin transliteration of word with attention to case
    :rtype: str
    """
    word = diddle_latin(word)
    word = word[0].upper() + word[1:].lower()
    return word


# place your code for experimenting here (will not be tested)
if __name__ == '__main__':
    pass
