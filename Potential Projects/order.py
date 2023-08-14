#  create a function called order_meal to handle a user ordering a meal in a restaurant.
# The function should take a single argument, num_people, which is the number of people ordering a meal.
# The function should then ask each person for their order, and collect the order for each person in a dictionary.

def order_meal(num_people): # num_people is the parameter
    menu = { 
        "starters": ["Soup", "Salad", "Bruschetta", "Spring Rolls"],  # starter is the key and the list is the value
        "mains": ["Steak", "Pasta", "Fish and Chips", "Vegetable Curry"], # main is the key and the list is the value
        "desserts": ["Cheesecake", "Tiramisu", "Ice Cream", "Fruit Salad"] # dessert is the key and the list is the value
    }

    orders = [] # empty list

    for person in range(1, num_people + 1): 
        print(f"Ordering for person {person}:") 
        # Ask for starter choice
        print("Choose a starter:")
        for i, starter in enumerate(menu["starters"], start=1):
            print(f"{i}. {starter}")
        starter_choice = int(input())
        selected_starter = menu["starters"][starter_choice - 1]

        # Ask for main course choice
        print("Choose a main course:")
        for i, main in enumerate(menu["mains"], start=1):
            print(f"{i}. {main}")
        main_choice = int(input())
        selected_main = menu["mains"][main_choice - 1]

        # Ask for dessert choice
        print("Choose a dessert:")
        for i, dessert in enumerate(menu["desserts"], start=1):
            print(f"{i}. {dessert}")
        dessert_choice = int(input())
        selected_dessert = menu["desserts"][dessert_choice - 1]

        # Ask for drink choice - This is not in the menu dictionary, so we don't need to loop through it, we can just ask for input
        print("Choose a drink:")
        drink_choice = input()

        # Collect the order for this person. We can use a dictionary to store the order for this person
        person_order = {
            "Person": person,
            "Starter": selected_starter,
            "Main Course": selected_main,
            "Dessert": selected_dessert,
            "Drink": drink_choice
        }
        orders.append(person_order) # append the person_order dictionary to the orders list

    # Display the complete order
    print("\nOrder Summary:")
    for order in orders:
        displayOrder(order)

def displayOrder(order):
    print(f"Person {order['Person']} ordered:")
    print(f"Starter: {order['Starter']}")
    print(f"Main Course: {order['Main Course']}")
    print(f"Dessert: {order['Dessert']}")
    print(f"Drink: {order['Drink']}")
    print("------------------")

# Example usage:
order_meal(2)  # For 2 people ordering their meals
