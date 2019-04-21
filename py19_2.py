#!/usr/bin/env python3

# this is the program to determine the number of character from different categories, like digit, space, or letter.

def count(*param):
    length = len(param)
    for i in range(length):
        letters = 0
        space = 0
        digit = 0
        others = 0
        for each in param[i]:
            if each.isalpha():
                letters += 1
            elif each.isdigit():
                digit += 1
            elif each == ' ':
                space += 1
            else:
                others += 1

        print("The {0}th character contains: letters {1}, digit {2}, space {3}, and others {4}.".format(i, letters, digit, space, others))


count('I love fish.com.', 'I love you, you love me.')

count('89899889', 'No wonder *** I love you 2')
