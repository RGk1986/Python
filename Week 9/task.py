
# fruits_list = ['apple', 'banana', 'orange', 'grape', 'mango']

# second_fruit = fruits_list[1]
# print(second_fruit)  # Output: 'banana'

# colors_tuple = ('red', 'blue', 'green', 'yellow', 'purple')
# third_color = colors_tuple[2]
# print(third_color)  # Output: 'green'

# person_dict = {
#     'name': 'John Doe',
#     'age': 30,
#     'occupation': 'Engineer',
#     'location': 'New York'
# }
# person_name = person_dict['name']
# print(person_name)  # Output: 'John Doe'

# languages_set = {'Python', 'JavaScript', 'Java', 'C++', 'Python'}
# import random
# random_language = random.choice(list(languages_set))
# print(random_language)  # Output: Could be 'Python', 'JavaScript', 'Java', 'C++', or any other language in the set.

# list1 = [] # Declare list1 variable and assign it the list data type
# list2 = ["HTML", "CSS", "JavaScript", "Python"] # Declare list2 variable and assign it the list data type
# print(list1) # Print out the value of list1

# list1.append("Java") # Add Java to the end of the list
# print(list1) # Print out the value of list1

# list2.insert(0, "C#") # Insert C# at index 0
# print(list2) # Print out the value of list2

# # Access list items using their index
# #           0      1       2       3       4
# list3 = ["Dave", "Rob", "John", "Steve", "Skye"]
# print(list3[4]) # Print out the value at index 4

# tuple1 = ("Paul", "John", "George", "Ringo") # Declare tuple1 variable and assign it the tuple data type
# # How do we access tuple items? print(tuple1[1]) # Print out the value at index 1

# # slicing a list or tuple
# # list[start:end:step]
# # tuple[start:end:step]
# # start is inclusive

# print(list3[0:3]) # Print out the values from index 0 to index 2
# print(list3[0:5:2]) # Print out the values from index 0 to index 4 in steps of 2
# print(list3[:2]) # Print out the values from index 0 to index 2
# print(list3[::2]) # Print out the values from index 0 to index 4 in steps of 2
# print(list3[::-1]) # Print out the values from index 0 to index 4 in steps of 2


# ~list exercise

# create a list of 6 items
print ("Creating a list of 6 random items")
exList = ["Grapefruit", "Bicycle", "Mountain", "Towel", "Beacon", "Spaceship"]
print (exList)

# insert a new item in position 3
exList.insert(3, "Sword")
print ("Inserted Sword at position 3")
print (exList)

# add another item to the list
exList.append("Pencil")
print ("Appending Pencil to the end of the list")
print (exList)

# remove an item by value
exList.remove("Mountain")
print ("Removing Mountain from the list")
print (exList)

# remove the item at index position 3
exList.pop(3)
print ("Popping the item at index position 3")
print (exList)

# for every list manipulation print the list

s5 = "It is a beautiful day in the neighborhood"
print(s5)
print(s5[0:5])
print(s5[0:5:2])
print(s5[0:5:3])

