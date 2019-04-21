#!/usr/bin/env python3

# 密码安全性检查代码
#
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
#
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位
#
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位


symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'

passwd = input("Please enter the password that you want to verify the strength for: ")

# judge the length of the password

length = len(passwd)

while (passwd.isspace() or length ==0 or passwd[0]=='*'):
    passwd = input("You've entered spaces or nothing. Please retry: ")
    length = len(passwd)

if length <= 8:
    flag_len = 1
elif 8 < length < 16:
    flag_len = 2
else:
    flag_len =3

flag_con = 0     

# judge if there is any special characters

for each in passwd:
    if each in symbols:
        flag_con += 1
        break

# 判断是否包含字母
for each in passwd:
    if each in chars:
        flag_con += 1
        break

# judge if there is any number in the password

for each in passwd:
    if each in nums:
        flag_con += 1
        break

# display the result of verification

while True:
    print("the security level of Password is: ", end=' ')
    if flag_len ==1 or flag_con == 1:
        print("low")
    elif flag_len ==3 and flag_con ==3 and (passwd[0] in chars):
        print("High")
        print("Please keep this way")
        break
    else:
        print("middle","length ={0}".format(flag_len),"flag_complication = {0}".format(flag_con))

    print("请按以下方式提升您的密码安全级别：\n\
    \t1. 密码必须由数字、字母及特殊字符三种组合\n\
    \t2. 密码只能由字母开头\n\
    \t3. 密码长度不能低于16位")
    break
