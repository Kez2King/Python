#Lists

    # How to create
#   - Lists are zero based

# grocery_list = ["Milk", "Eggs", "Bread", "Salmon", "Burgers", "Rebel IceCream"]
# print(grocery_list)

# How to access values

    # print(grocery_list[1]) # Prints of the specific item using it position
    # print(grocery_list[-2]) 
    # print(grocery_list[-3])

# How to add to lists

# pizza = ["cheese","pineapples", "anchoives", "Tuna"]
# pizza.append("Bacon") #Adds to the end of the list
# print(pizza)

# How to remove

# pizza.pop() # Removes the last item on the list by default
            # Place an integer/ index to be specific
    # or 
# del pizza[2] # Removes a specific item using its position using []
# print(pizza)

# Create To Do List w/ at least 7 initial item
ToDo_List = ["Shower", "Brush your teeth", "Eat breakfast", "Exercise"
, "Eat lunch", "Go on a run", "Eat dinner"]
print(ToDo_List)
# Display the 3rd and 5th items
print(ToDo_List[2])
print(ToDo_List[4])

# Display the second to last items, accessing from the end
print(ToDo_List[-2])

# Add 2 more items
ToDo_List.append("Shower")
ToDo_List.append("Sleep")

# Display items
print(ToDo_List)

# Remove the last item
ToDo_List.pop()

# Display items
print(ToDo_List)

# Change 2nd item to "Walk the dog"
ToDo_List[1] = "Walk the Dog"
print(ToDo_List)