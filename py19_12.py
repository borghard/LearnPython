#!/usr/bin/env python3

# 另一种方法检查回文字符串

def palindrome(string):
    length = len(string)
    length -= 1
    list1 = list(string)
    index = 0
    last = length
    flag = 1
    for i in range(length):
        if list1[index] == list1[last]:
            index += 1
            last -= 1
        else:
            flag = 0
    return flag

string = input("please enter a string: ")
if palindrome(string) == 1:
    print("this is a palindrome string.")
else:
    print("this is not a palindrome.")
    print("test result is: ",palindrome(string))

    
        
