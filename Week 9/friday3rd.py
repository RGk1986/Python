# sourcery skip: use-fstring-for-formatting
"""In Python, string handling, membership testing, global keyword, and scope are fundamental concepts related to 
manipulating strings, checking membership in data structures, and managing variable scopes. Let's briefly explain each of these concepts:

1. String Handling:
String handling refers to the manipulation and processing of strings, which are sequences of characters in Python. 
Python provides numerous built-in methods and operations for string handling, such as concatenation, slicing, formatting, searching, replacing, and more.

Example:

"""

# Concatenation
str1 = "Hello"
str2 = "World"
result = f"{str1} {str2}"

# Slicing
s = "Python"
print(s[1:4])  # Output: "yth"

# Formatting
name = "Alice"
age = 25
message = "My name is {} and I am {} years old.".format(name, age)
print(message)  # Output: "My name is Alice and I am 25 years old."

"""
2. Membership Testing:
Python allows you to check if an element exists in a data structure (like a list, tuple, set, or string) 
using the `in` keyword. This membership test returns a Boolean value (True or False).

Example:
"""
my_list = [1, 2, 3, 4, 5]

# Membership testing
print(3 in my_list)  # Output: True
print(6 in my_list)  # Output: False

"""
3. Global Keyword:
In Python, the `global` keyword is used to declare a variable as global inside a function. 
When a variable is declared as global, it means that the variable is not local to the function and can be accessed and modified from both inside and outside the function.

Example:
"""

global_variable = 10


def my_function():
    global global_variable
    global_variable += 1
    print(global_variable)


my_function()  # Output: 11
print(global_variable)  # Output: 11

"""
4. Scope:
Scope in Python refers to the visibility and accessibility of variables within a program. 
Python follows a rule of LEGB for variable scope, which stands for Local, Enclosing, Global, and Built-in. 
This means that Python will first search for a variable in the local scope, then in the enclosing (non-local) functions, then in the global scope, and 
finally in the built-in scope (pre-defined Python functions and modules).

Example:
"""

global_variable = 10  # Global scope


def my_function():
    local_variable = 20  # Local scope
    print(local_variable)  # Output: 20
    print(global_variable)  # Output: 10


my_function()
print(global_variable)  # Output: 10
"""
Keep in mind that if you want to modify a global variable inside a function, you must use the `global` keyword to 
indicate that you want to refer to the global variable, as shown in the example above. Otherwise, Python will create a new local variable instead of modifying the global one."""
