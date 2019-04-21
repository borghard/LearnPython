#!/usr/bin/env python3

def funX():
    x = 5
    def funY():
        nonlocal x
        x += 1
        print("I am here, now X is: {0}".format(x))
        return x
    return funY

a = funX()
print(a())
print(a())
print(a())
