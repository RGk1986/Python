# functions must have a RETURN statement
# Return statement is the last statement in the function, it returns a value to the caller
# It also stops the execution of the function

"""
function is a Sequence of instructions/code block to perform a specific task with 
an identifiable name
A function must have a return statement
def keyword is used to define a function, followed by the name of the function
A function is not executed unless it is invoked/called

"""

def addition ():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("The sum (addition) of the two numbers is: ", a + b)
    return a + b

sum = addition()

calc = sum * 50

"Method 1"
print(f"The answer is {addition()}")

"Method 2"
myAddition = addition()
print(f"The answer is {myAddition}")

# Exercise: modify the subroutine below to become a function
# Then make the code as concise as possible

def userName(): 
    fullName = input("What is your full name? ")
    address = input("What is your address? ")
    interest = input("What are your interests? ")
    print(f"My name is {fullName}, I live at {address} and my interests are {interest}.")

# Creating a function
def get_user_info():
    fullName = input("What is your full name? ")
    address = input("What is your address? ")
    interest = input("What are your interests? ")
    return f"My name is {fullName}, I live at {address}, and my interests are {interest}."

print(get_user_info())

#Refactoring to minimize code use

def get_user_info():
    return f"My name is {input('What is your full name? ')}, I live at {input('What is your address? ')}, and my interests are {input('What are your interests? ')}."

print(get_user_info())


# Use the argument to pass a number of values/parameters to a function/parameter
def addition2(*argNums):
    
    for nums in argNums:
        print(nums)
        
    answer = argNums[0] + argNums[1]
    print(answer)
    
addition2(2, 3, 4, 5, 6, 7, 8, 9, 10)

