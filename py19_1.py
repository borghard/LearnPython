#!/usr/bin/env python3

# to create an application to verify if a string is palindrome string

def palindrome(string):
    length = len(string)
    flag = 0
    last = length - 1
    string_1 = list(string)
    string_compare = []
    while string_1:
        for each in string_1:
            string_compare.append(string_1.pop())

    if string_compare == list(string):
        flag = 1

    else:
        flag = 0

    return flag

string = input("please enter a string: ")
if palindrome(string) == 1:
    print("this is a palindrome string.")
else:
    print("this is not a palindrome.")
    print("test result is: ",palindrome(string))


    
    
         
        
