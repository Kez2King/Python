# Sequences

# Lists - MUTABLE: Can be changed

# list_of_numbers = [123 , 456]
# list_of_numbers[0] = 'abc'
# print(list_of_numbers)

# Tuple - IMMUTABLE: Cannot change the values

# coordinate = (123.45, 567.89)
# coordinate[0] = "abc"
# print(coordinate)

# Ranges
# range(start, stop, step)

# this_range = range(10)
# print(this_range)

# Create a list w/ 5 values: Later use
list_of_values = [13, 77, 87, 22, 73]

# Change value of the item in the middle of the list to a tuple
list_of_values[2] = (8, 5, 6)
print(list_of_values)

# Create a range of intergers to the number 7 & add it to a variable
my_range = range(8)

# Add range of integers you just created to the end of the initial list
list_of_values.append(my_range)
print(list_of_values)

# Display the middle value in the list
print(list_of_values[2])

# Display the last value in the list
print(list_of_values[-1])