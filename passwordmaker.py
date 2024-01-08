## Develop a simple Passwordmaker ##

import random
import string


# Define characters
lowercase_chrs = string.ascii_lowercase #abcdefghijklmnopqrstuvwxyz
uppercase_chrs = string.ascii_uppercase #ABCDEFGHIJKLMNOPQRSTUVWXYZ
symbols = "~!@#$%^&*()_-+={}[]<>?"
numbers = ''.join([str(i) for i in range(0, 10)]) #0123456789

all_ = lowercase_chrs + uppercase_chrs + symbols + numbers

# Define main loop

while True:

    print("Please choose your strategy:\n\t1) Create Password\n\t2) Exit")

    user_input = input('Your choice is: ')

    print()
    print("-" * 40)
    if user_input == '1':

        pass_len = int(input("Enter your password length:")) # for example: pass_len = 12
        password = ''.join([random.choice(all_) for i in range(0, pass_len)]) # tDX-%@5?utgw
        #password = ''.join(random.sample(all_, pass_len)) #tDX-%@5?utgw
        print(f'Your password is: {password}')
        print('=' * 40)
        continue

    elif user_input == '2':

        print("You are going to exit the program")

        break

    else:
        print("Wrong choice. Try Again!")
        print("*"*40)
        continue



