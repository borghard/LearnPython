#!/usr/bin/env python3

# find the password from the string
''' a) 每位密码为单个小写字母
    b) 每位密码的左右两边均有且只有三个大写字母
    '''

str1 = input("Plesae enter the string of password: ")

countA = 0 # statistic the number of captial letters at left side
countB = 0 # statistic the number of lower letters
countC = 0 # statistic the number of captial letter at right side

length = len(str1) - 1
passw = []
flag_1 = 0

for i in range(3,length-2):
    if str1[i] == '\n':
        continue

    if str1[i].islower():
        x = 3
        while x:
            if str1[i+x].isupper() and str1[i-x].isupper():
                x -= 1
                flag_1 = 0 
            else:
                x = 0
                flag_1 = 1
        if flag_1 == 0:
            passw.append(str1[i])

print("the password is: ", end='')
for each in passw:
    print(each, end='')
    
        
                
