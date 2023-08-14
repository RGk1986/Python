"Exercise"

# Create two variables fName and lName and join and print them using a variable called fullName


fname = input("What is your name?:")
lname = input("What is your last name?:")
fullname = f'{fname} {lname}'
print(f"So your name is {fullname}")


course = "Python"
print(course[-6:]) # This is called slicing, it starts from the end of the string and goes back 6 characters then prints the rest of the string



wordlength = len(course)
print(wordlength)


"Exercise:"
# The code is asking you to perform some comparison operations using comparison operators. You need to
# compare the following:

#  use any comparison operator to compare the letter "a" and "A"
result1 = "a" == "A"
print(result1)  # Output: False

#  use any comparison operator to compare the letters "ax" and "ZZ"
result2 = "ax" != "ZZ"
print(result2)  # Output: True

#  use any comparison operator to compare your firstname with any another first name
your_firstname = "Rob"
other_firstname = "Jean"
result3 = your_firstname < other_firstname
print(result3)  # Output: True or False, depending on the input arguments



name = "Tim is Software Technical Trainer"
for letter in name:
    print(letter)


searchStr = "Python is a great programming language"
findChar = input("Enter character to search for: ") #i

"""The membership operator can be used to check if a value/substring is present 
or not in object and returns true if it does"""
if findChar in searchStr:  # opposite of the in operator is the 'not in'
    print(f"Found {findChar}")
else:
    print(f" Not Found")

"Exercise: replace the in operator with the 'not in' operator "
if findChar not in searchStr:  # opposite of the in operator is the 'not in'
    print(f"Found {findChar}")
else:
    print(f" Not Found")

