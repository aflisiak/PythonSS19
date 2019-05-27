"""
Universität Tübingen - Seminar für Sprachwissenschaft
VL 'Programming and Data Analysis' SS 2019
© Johannes Dellert, Maxim Korniyenko, Natalie Clarius, Gerhard Jäger

Assignment 00: Ungraded Test Assignment
Template
"""

# This is part of the program initialization, we will use it to test your code on different three-word sentences.
# You can also assign different values to these variables in order to test your code.
if "word1" not in vars():
    word1 = "we"
    word2 = "are"
    word3 = "programming"

# This is the block in which your code must reside (in place of the current 'pass' statement).
if __name__ == '__main__':
    # Task 1: Adding word lengths:
    word_len = len(word1 + word2 + word3)  # 16
    print("Sentence: \"{} {} {}\", overall length: {}".format(word1, word2, word3,
                                                              word_len))  # prints: Sentence: "we are programming", overall length: 16

    # Task 2: Computing percentages:
    word1_p = len(word1) / word_len  # 0.125
    word2_p = len(word2) / word_len  # 0.1875
    word3_p = len(word3) / word_len  # 0.6875
    print("Word length percentages: {}%, {}%, {}%".format(int(word1_p * 100), int(word2_p * 100), int(word3_p * 100)))

    # Task 3: Measuring unbalancedness
    unbalancedness = (word1_p - 1 / 3) ** 2 + (word2_p - 1 / 3 ** 2) + (word3_p - 1 / 3 ** 2)  # 0.6961805555555555
    print("Unbalancedness: {}".format(unbalancedness))
