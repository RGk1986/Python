"""
In this example, the function display_info takes two mandatory arguments 
(name and age) using 
*args to handle additional positional arguments and **kwargs to handle additional keyword arguments.
"""

def display_info(name, age, *args, **kwargs):
    print(f"Name: {name}")
    print(f"Age: {age}")

    # Check if any additional positional arguments were passed
    if args:
        print("Additional Positional Arguments:")
        for arg in args:
            print(arg)

    # Check if any additional keyword arguments were passed
    if kwargs:
        print("Additional Keyword Arguments:")
        for key, value in kwargs.items():
            print(f"{key}: {value}")

# Using the function with both positional and keyword arguments
display_info("John", 30, "Engineer", "New York", company="ABC Corp", salary=60000)


"""
As you can see, *args collects the additional positional arguments 
("Engineer" and "New York") and **kwargs collects the additional keyword 
arguments (company="ABC Corp" and salary=60000), and the function displays
them accordingly. This combination of *args and **kwargs gives your 
function even more flexibility when handling varying types of arguments.
"""