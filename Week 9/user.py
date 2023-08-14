def addition ():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("The sum (addition) of the two numbers is: ", a + b)
    

def subtraction ():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("The sum (subtraction) of the two numbers is: ", a - b)

    
def multiplication ():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("The sum (multiplication) of the two numbers is: ", a * b)


def division ():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("The sum (division) of the two numbers is: ", a / b)


# call: addition()
# call: subtraction()
# call: multiplication()
# call: division()

# # "Method 1"
# # in the subroutine call pass in the argument that will pass into the parameterFname
# fName("Bob") # My firstname is Bob

# # "Method 2"
# # use the input to ask for the value that will be saved in the argFirstname variable

# argFirstname = input("What is your first name?:")

# # in the subroutine call pass in the variable argFirstname as argument
# fName(argFirstname) # My firstname is "inputValue"

# # "Method 3"
# fName(input("Enter your first name? "))  # the input is passed in as an argument

# Modify the code below to use parameters(arguments)
# Define a subroutine called userName

def username(fname, lname, interests):
    # print("What is your first name?")
    # fname = input()
    # print("What is your last name?")
    # lname = input()
    fullname = fname + " " + lname
    # print("What are your interests?")
    # interests = input()
    print("My name is " + fullname + " and my interests are " + interests + ".")
    