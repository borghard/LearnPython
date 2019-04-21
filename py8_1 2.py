#！/usr/bin/env python3

#define the Password

password = 'IloveCatherine'
count = 3 #how many time are allowed to try

# define the verification function

def validationpassword(a):
    if a == 'IloveCatherin':
        return True
    else:
        return False


while count > 0:
    guess = str(input("please enter the password: "))

    if validationpassword(guess) == False:
        print("Sorry, wrong guess! Please enter again!")
        count -= 1
        guess=str(input("try again, you have %d chances left." % count))

    print("Good!
        
