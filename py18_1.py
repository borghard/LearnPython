#!/usr/bin/env python3

def multiplebase(base):
    '''函数返回列表中数字之和乘以3的积。如果最后一位是5，那么技术变为5，但5不参与合计'''
    a = 3

    if base[len(base)-1] == 5:
        a = 5
    temp = 0 
    for each in base:
        temp += each

    if a != 5:
        return temp * a
    else:
        return (temp - 5) * a

x = input('please enter a list: ')
xlist = x.split(",")
print("xlist = ", xlist)
xlist = [int(xlist[i]) for i in range(len(xlist))]
print("result of the calculation of list is: ", multiplebase(xlist))

        
