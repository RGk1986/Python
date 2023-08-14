"""
Exercise 1 : Character Input (PracticePython.org)

Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. 
Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year). If you want to do this in a generic way, see exercise 39.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

"""

userName = input("Enter your name: ")
age = int(input("Enter your age: "))
copies = int(input("Enter the number of copies: "))

def when100():
    year = 2023 + (100 - age)
    print(f"{userName}, you will be 100 years old in {year}.")
    return 

for _ in range(copies):
    when100()
    print("\n")


"""
Exercise 2 : Odd Or Even (PracticePython.org)

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.

Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

userNum = int(input("Enter a number: "))
userCheck = int(input("Enter a number to divide by: "))
userSum = userNum / 2
userCheckSum = userNum / userCheck

def oddoreven():
    if userSum % 2 == 0:
        print(f"{userNum} is an even number.")
    else:
        print(f"{userNum} is an odd number.")
    return

def multipleof4():
    if userNum % 4 == 0:
        print(f"{userNum} is a multiple of 4.")
    else:
        print(f"{userNum} is not a multiple of 4.")
    return

def userDiv():
    if userCheckSum == 0:
        print(f"{userCheck} divides evenly into {userNum}.")
    else:
        print(f"{userCheck} does not divide evenly into {userNum}.")
    return

oddoreven()
multipleof4()
userDiv()

""" 
Exercise 3 : List Less Than Ten (PracticePython.org)

Take a list and write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.

Write this in one line of Python.

Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Creating a subroutine to print out all the elements of the list that are less than 5

def lessThan5():
    for num in a:
        if num < 5:
            print(num)
    return

lessThan5()

# Create a subroutine to print out all the elements of the list less than a user input number

def lessthanuser():
    userNum = int(input("Enter a number: "))
    for num in a:
        if num < userNum:
            print(num)
    return

lessthanuser()

# Printing anything less than or equal to 5 from the list in one line of code.

print([num for num in a if num <= 5])

# Printing anything less than or equal to a user input number from the list in one line of code.

print([num for num in a if num <= int(input("Enter a number: "))])

"""
Exercise 4 : Divisors (PracticePython.org)
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

userNum = int(input("Enter a number: "))

def divisors():
    for num in range(1, userNum + 1): # The range function is exclusive of the last number, so we add 1 to the user input number to include it. 
                                      # Here we are using it to iterate through all the numbers from 1 to the user input number.
        if userNum % num == 0:        # If the user input number divided by the number in the range has no remainder, then it is a divisor of the user input number.
            print(num)
    return

divisors()

"""
Exercise 5 : List Overlap (PracticePython.org)

Take two lists, say for example these two:

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this

Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def commonElements():
    for num in a:
        if num in b:
            print(num)
    return

commonElements()

# Generating two lists of random numbers and printing out the common elements in one line of code.

import random

c = random.sample(range(1, 100), 10)
d = random.sample(range(1, 100), 10)

print([num for num in c if num in d])

""" 
Exercise 6 : String Lists (PracticePython.org)

Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""

def palindrome():
    userString = input("Enter a string: ")
    if userString == userString[::-1]: # The [::-1] is a slice that reverses the string.
        print("This string is a palindrome.")
    else:
        print("This string is not a palindrome.")
    return

palindrome()
