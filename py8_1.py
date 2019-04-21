#!/usr/bin/env python3
# This is to design a program to let player to guess the password. 
# count of times that the player tries to guess. 3 at max
count = 3

# Password

password = 'IloveCatherine'

while count > 0:
    guess = str(input("Plesae give your guess: "))
    if '*' in guess:
        print("No * is allowed in a password. Please retry")
        continue
    else:
        if guess == password:
            print("Congratulations! You've given the correct password.")
            break
        if guess != password:
            print("Sorry, you've made a wrong guess. You have other {0} time of chances left. Please try again!".format(count))
            count -= 1
            if count == 0:
                print("Sorr you've used up your chances!")
            continue

print("Game Over")
        
        
        

