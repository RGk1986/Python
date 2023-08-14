"""
Claude's list of great ideas(He is stupid and I hate him):

- Create a separate Menu class to encapsulate the menu options. This avoids hardcoding the options in the order_meal function.

- Create an Order class to represent an order for a single person. This can encapsulate the person's choices.

- Use better names like get_order instead of order_meal and print_order instead of displayOrder.

- Split order_meal into smaller functions:

    print_menu to print the menu options
    get_choice to get a single menu choice
    get_order to get the order for one person
    print_orders to print a summary of all orders

- Store the menu as a nested dictionary rather than individual variables for each course.

- Use constants for fixed values like menu categories instead of hardcoding strings.

- Validate input rather than just converting to int which could crash.

- Use f-strings or .format() for cleaner string formatting.

- Add type hints for function parameters and returns.

- Add docstrings explaining each function.

- Use better data structures like a custom Order class rather than a plain dictionary.

The key points are to break into smaller functions with focused responsibilities, use better names, 
validate data, remove duplication, and leverage classes and objects more effectively.

These points, Google, some explanations like I was 5, and some sheer dumb luck, and I was able to create the below.
"""

# Classes in Python are used to create objects. An object is an instance of a class. for example, if we have a class called Person, we can create an object of type Person, which is an instance of the Person class.
# Classes are used to group related data and functions together. For example, a Person class might have data such as name, age, address, etc. and functions such as walk(), talk(), eat(), etc.
# Classes are defined using the class keyword, followed by the name of the class. The name of the class should be in PascalCase, which means that each word in the name should start with a capital letter.
class Menu:
    # Constants for menu categories
    STARTERS = "starters"
    MAINS = "mains"
    DESSERTS = "desserts"
# The __init__() function is a special function that is called when an object is created. It is used to initialize the object with some data. It is also called the constructor function.
    def __init__(self):
        self.menu_options = {
            self.STARTERS: ["Soup", "Salad", "Bruschetta", "Spring Rolls"],
            self.MAINS: ["Steak", "Pasta", "Fish and Chips", "Vegetable Curry"],
            self.DESSERTS: ["Cheesecake", "Tiramisu", "Ice Cream", "Fruit Salad"]
        }
# the print_menu() function prints the menu options to the screen. This was important, and not super easy to figure out.
    def print_menu(self):
        print("Menu Options:")
        for category, options in self.menu_options.items():
            print(f"{category.capitalize()}:")
            for i, option in enumerate(options, start=1):
                print(f"{i}. {option}")
            print()
# The get_choice() function takes a category as an argument and returns the user's choice from that category.
    def get_choice(self, category):
        options = self.menu_options[category]
        print(f"{category.capitalize()}:")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        while True:
            try:
                choice = int(input(f"Choose a {category}: "))
                if 1 <= choice <= len(options):
                    return options[choice - 1]
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Invalid input. Try again.")


class Order:
    def __init__(self, person_num):
        self.person_num = person_num
        self.starter = None
        self.main_course = None
        self.dessert = None
        self.drink = None
# the __str__() function is a special function that is called when an object is converted to a string. It is used to return a string representation of the object.
    def __str__(self):
        return f"Person {self.person_num} ordered:\n" \
               f"Starter: {self.starter}\n" \
               f"Main Course: {self.main_course}\n" \
               f"Dessert: {self.dessert}\n" \
               f"Drink: {self.drink}\n" \
               "------------------"

# get_order() is a function that returns an Order object it takes a Menu object and a person number as arguments. 
# It uses the Menu object to get the user's choices for each course and the person number to display the correct person number in the order.
# The function returns an Order object with the user's choices.
def get_order(menu: Menu, person_num: int) -> Order:
    order = Order(person_num)
# Here we are using the print function to print the options for the person number, and then we are using the menu object to get the user's choices for each course.
    print(f"\nOptions for Person {person_num}:")
    order.starter = menu.get_choice(Menu.STARTERS)
    order.main_course = menu.get_choice(Menu.MAINS)
    order.dessert = menu.get_choice(Menu.DESSERTS)
    order.drink = input("Choose a drink: ")
    return order

# print_orders() is a function that prints the orders which allows the user to see what they have ordered.
def print_orders(orders):
    print("\nOrder Summary:")
    for order in orders:
        print(order)

# get_num_people() is a function that returns the number of people ordering, this is used to create the correct number of Order objects.
def get_num_people() -> int:
    while True:
        try:
            num_people = int(input("Enter the number of people ordering: "))
            if num_people > 0:
                return num_people
            else:
                print("Invalid input. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# get_orders() is a function that returns a list of Order objects.
def get_orders() -> list[Order]:
    num_people = get_num_people()
    menu = Menu()
    return [get_order(menu, person_num) for person_num in range(1, num_people + 1)] # this return statement uses a list comprehension so that the list of Order objects is created in one line.


# The following code is executed when the program is run
# It is not executed when the program is imported as a module
# This is useful for testing your code
# You can also use this area to write your own tests, if you wish
if __name__ == "__main__":
    orders = get_orders()
    print_orders(orders)
    