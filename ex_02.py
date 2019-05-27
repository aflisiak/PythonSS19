"""
Universität Tübingen - Seminar für Sprachwissenschaft
VL 'Programming and Data Analysis' SS 2019
© Johannes Dellert, Maxim Korniyenko, Natalie Clarius, Gerhard Jäger

Assignment 02: Paradigm generation for Turkish
Template
"""


def is_vowel(letter):
    """
    Checks whether the sound is a vowel.
    :param letter: the letter to be checked
    :type letter: str
    :return: true if letter is a vowel
    :rtype: bool
    """
    vowels = "A", "a", "E", "e", "I", "ı", "İ", "i", "O", "o", "U", "u", "Ö", "ö", "Ü", "ü"
    if letter in vowels:
        return True
    else:
        return False


def ends_in_vowel(word):
    """
    Checks whether the words ends with a vowel sound.
    :param word: the word to be checked
    :type word: str
    :return: true if the word ends with a vowel sound
    :rtype: bool
    """
    vowels = "A", "a", "E", "e", "I", "ı", "İ", "i", "O", "o", "U", "u", "Ö", "ö", "Ü", "ü"
    if word[-1] in vowels:
        return True
    else:
        return False


def get_last_vowel(word):
    """
    Returns the last vowel in a word.
    NOTE: Since we didn't make sure that the characters at indices -1, -2 and -3 actually exist,
    i.e. that word has at least length 1/2/3, this function will result in an error for words with 0 < len(word) < 3.
    :param word: the word to retrieve the last vowel from
    :type word: str
    :return: the last vowel in word
    :rtype: str
    """
    if len(word) < 0:
        return None
    else:
        if is_vowel(word[-1]):
            return word[-1]
        elif is_vowel(word[-2]):
            return word[-2]
        elif is_vowel(word[-3]):
            return word[-3]
        else:
            return None


def is_voiced(consonant):
    """
    Checks whether the consonant is voiced.
    :param consonant: the consonant to be checked for voiceness
    :type consonant: str
    :return: true if consonant is voiced
    :rtype: bool
    """
    voiced_consonants = "b", "c", "d", "g", "ğ", "j", "l", "m", "n", "r", "v", "y", "z"
    if consonant in voiced_consonants:
        return True
    else:
        return False


def i_type_harmony(vowel):
    """
    Returns the I-type harmonic counterpart vowel to the given vowel.
    :param vowel: the vowel to retrieve the harmonic vowel for
    :type vowel: str
    :return: the appropriate harmonic counterpart to vowel according to the rules of I-type harmony
    :rtype: str
    """
    return_ü = "ö", "ü"
    return_u = "o", "u"
    return_i = "e", "i"
    return_ı = "a", "ı"
    if vowel in return_ü:
        return "ü"
    elif vowel in return_u:
        return "u"
    elif vowel in return_i:
        return "i"
    elif vowel in return_ı:
        return "ı"
    else:
        return None


def a_type_harmony(vowel):
    """
    Returns the A-type harmonic counterpart vowel to the given vowel.
    :param vowel: the vowel to retrieve the harmonic vowel for
    :type vowel: str
    :return: the appropriate harmonic counterpart to vowel according to the rules of A-type harmony
    :rtype: str
    """
    return_e = "e", "i", "ö", "ü"
    return_a = "a", "ı", "o", "u"
    if vowel in return_e:
        return "e"
    elif vowel in return_a:
        return "a"
    else:
        return None


def consonant_harmony(noun):
    """
    Returns the appropriate consonant 'd' or 't' for the noun according to the rules of consonant harmony.
    :param noun: the noun to retrieve the harmonic consonant for
    :type noun: str
    :return: the appropriate consonant 'd' or 't' depending on the last sound of noun
    :rtype: str
    """
    if is_voiced(noun[-1]) or ends_in_vowel(noun[-1]):
        return "d"
    else:
        return "t"


def inflect_noun(lemma, case, number):
    """
    Inflect the given lemma using the morphological rules of Turkish language.
    :param lemma: the lemma to be inflected
    :type lemma: str
    :param case: the case (NOM/ACC/GEN/...) to be inflected for
    :type case: str
    :param number: the number (singular/plural) to be inflected for
    :type number: str
    :return: the inflected noun
    :rtype: str
    """
    if number is "singular":
        if case is "NOM":
            noun = lemma
            return noun
        elif case is "ACC":
            if ends_in_vowel(lemma):
                noun = lemma + "y" + "i"
            else:
                noun = lemma + "i"
            return noun
        elif case is "GEN":
            if ends_in_vowel(lemma):
                noun = lemma + "y" + "in"
            else:
                noun = lemma + "in"
            return noun
        elif case is "DAT":
            if ends_in_vowel(lemma):
                noun = lemma + "y" + "e"
            else:
                noun = lemma + "e"
            return noun
        elif case is "LOC":
            noun = lemma + consonant_harmony(lemma) + "e"
            return noun
        elif case is "ABL":
            noun = lemma + consonant_harmony(lemma) + "en"
            return noun
    elif number is "plural":
        if case is "NOM":
            if a_type_harmony(get_last_vowel(lemma)) is "a":
                suffix = "lar"
                noun = lemma + suffix
                return noun
            elif a_type_harmony(get_last_vowel(lemma)) is "e":
                suffix = "ler"
                noun = lemma + suffix
                return noun
        elif case is "ACC":
            if a_type_harmony(get_last_vowel(lemma)) is "a":
                suffix = "lar"
                noun = lemma + suffix + "i"
                return noun
            elif a_type_harmony(get_last_vowel(lemma)) is "e":
                suffix = "ler"
                noun = lemma + suffix + "i"
                return noun
        elif case is "GEN":
            if a_type_harmony(get_last_vowel(lemma)) is "a":
                suffix = "lar"
                noun = lemma + suffix + "in"
                return noun
            elif a_type_harmony(get_last_vowel(lemma)) is "e":
                suffix = "ler"
                noun = lemma + suffix + "in"
                return noun
        elif case is "DAT":
            if a_type_harmony(get_last_vowel(lemma)) is "a":
                suffix = "lar"
                noun = lemma + suffix + "e"
                return noun
            elif a_type_harmony(get_last_vowel(lemma)) is "e":
                suffix = "ler"
                noun = lemma + suffix + "e"
                return noun
        elif case is "LOC":
            if a_type_harmony(get_last_vowel(lemma)) is "a":
                suffix = "lar"
                noun = lemma + suffix + consonant_harmony(suffix) + "e"
                return noun
            elif a_type_harmony(get_last_vowel(lemma)) is "e":
                suffix = "ler"
                noun = lemma + suffix + consonant_harmony(suffix) + "e"
                return noun
        elif case is "ABL":
            if a_type_harmony(get_last_vowel(lemma)) is "a":
                suffix = "lar"
                noun = lemma + suffix + consonant_harmony(suffix) + "en"
                return noun
            elif a_type_harmony(get_last_vowel(lemma)) is "e":
                suffix = "ler"
                noun = lemma + suffix + consonant_harmony(suffix) + "en"
                return noun


def print_paradigm(lemma):
    """
    Print the full inflectional paradigm (all numbers and cases) of the lemma.
    :param lemma: the lemma to print the paradigm for
    :type lemma: str
    """
    print("\tSingular\t\tPlural")
    print("NOM\t{}\t\t{}".format(inflect_noun(lemma, "NOM", "singular"), inflect_noun(lemma, "NOM", "plural")))
    print("ACC\t{}\t\t{}".format(inflect_noun(lemma, "ACC", "singular"), inflect_noun(lemma, "ACC", "plural")))
    print("GEN\t{}\t\t{}".format(inflect_noun(lemma, "GEN", "singular"), inflect_noun(lemma, "GEN", "plural")))
    print("DAT\t{}\t\t{}".format(inflect_noun(lemma, "DAT", "singular"), inflect_noun(lemma, "DAT", "plural")))
    print("LOC\t{}\t\t{}".format(inflect_noun(lemma, "LOC", "singular"), inflect_noun(lemma, "LOC", "plural")))
    print("ABL\t{}\t\t{}".format(inflect_noun(lemma, "ABL", "singular"), inflect_noun(lemma, "ABL", "plural")))

    if __name__ == '__main__':
        pass
