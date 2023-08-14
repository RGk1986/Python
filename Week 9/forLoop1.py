print("For (value) in range(stop):")
for findnumber2 in range(15):
    print(findnumber2)

print("For (value) in range(start, stop):")
for findNumber in range(1, 10):
    print(findNumber)

print("For (value) in range(start, stop, step):")
for findnumber3 in range(1, 10, 2):
    print(findnumber3)
    
"""
Modify the code to create a countdown using start:stop:step
"""

print("Countdown")
for x in range(10, 0, -1):
    print(x)
print("Blastoff!")

   
# Complete the code below to iterate though both lists, add comment to explain your code 

# highscore = [125, 63, 35, 12]
# # "block of code is missing here"
# print(counter) # highscore[counter]

# usersList = ["Anna", "Paul", "Joe", "Jane", "Anne", "Pauline", "Joan", "Janet"]
# #"block of code is missing here"
# print(f"{users}")
    
    
highscore = [125, 63, 35, 12, 100, 200, 300, 400]
usersList = ["Anna", "Paul", "Joe", "Jane", "Anne", "Pauline", "Joan", "Janet"]

# Determine the length of the shorter list
length = min(len(highscore), len(usersList))

# Iterate through both lists using a range and length
for counter in range(length):
    score = highscore[counter]
    users = usersList[counter]
    # Print the score and the corresponding user's name
    print(f"{users} - Highscore: {score}")


""" Debug and fix the multiplication program below 
add comment where you fix the bugs
"""
# print("Welcome to the table quiz.\n")
# num = int(input("Enter a number: "))


# for : #1,2,3,4   
#     answer = int(input(f" What is {i} x {num}? "))
#     print(f"the answer is {answer} ")
#     correct = i * num
#     if answer == correct:
#         print("Correct")

#     else:
#         print(f"No, the answer is  {correct}")

# print("Finished")


print("Welcome to the table quiz.\n")
num = int(input("Enter a number: "))

for i in range(1, 11):  # Fix 1: Specified an end value for the range.
    answer = int(input(f"What is {i} x {num}? ")) 

    # Fix 3: Adjust the indentation for the following lines
    print(f"The answer is {answer}.")
    correct = i * num

    # Fix 4: Convert the user input to an integer before comparing it with correct
    if answer == correct:
        print("Correct")
    else:
        print(f"No, the answer is {correct}")
print("Finished")


# Complete the code below to display multiplication table of your choice
num1 = int(input("Enter a number for multiplication: "))
for num2 in range(1, 13):
    print(f"{num1} x {num2} = {num1 * num2}")

# While loops just continue to run until the condition is met

secretWord = "Python"
while True:
    userGuess = input("Guess my secret word: ")
    if userGuess == secretWord:
        print("You guessed it!")
        break  # Exit the loop if the user guessed correctly
    else:
        print("Sorry, try again.")
print("Finished")

"""
Use a while loop when the number of iteration is unknown(dont know how many times you want/going 
to do something for)
A while loop also controls the flow of execution in a program
"""


"""Comparison operator compare values
==    equal  ( 2 == 2)
< 	less than
> 	more than
<= 	less than or equal to 
>= 	greater than or equal to
!=    Not equal to"""

# While loop keeps looping/iterating until a condition is met
num = 1  # int(input("Enter number below 20: "))

while num <= 20:
    print(f"The number is {num}")
    num += 1  # what is this doing ? increments num by 1 every loop

"Exercise: Modify the code above to countdown from 20"

# "solution"
print("\ncountdown from 20")
num = 20
while num >= 0:
    print(f"The number is {num}")
    num -= 1  # what is this doing ? decrements num by 1 every loop


import random # import the random module
num = 1 
userNum = random.randint(1, 20) # generate a random number between 1 and 20
while num <= 20: # loop until num is greater than 20
    print(f"Guessing all possible numbers, currently at {num}") # print the current value of num with custom message
    if num == userNum: # if num is equal to the random number
        print("exiting the loop...") # then print a message
        break # and exit the loop
    num += 1  # What is this doing? This is increasing the value of num by 1 every loop
print("we have broken the loop") 


# Error Handling - try and except

# except(ValueError, IndexError, NameError):
    
# if ValueError:
#         print("Please enter a numberic value.")
# elif IndexError:
#         print("The following error occurred {e}")
# else NameError:
#         print("The following error occurred {e}")

name = input("Enter your name: ")

if name.istitle():
    print(f"Welcome, {name}, you have entered your name in the correct format.")
else:
    print("Please enter your name with a capital letter.")
exit()
