# string1 = "I'm a string"
# print(string1)
# string2 = "I'm a string" [::-1]
# print(string2)

"""
    [X] What is a function, Why would we want to use them?

        - A function creates a way to reference a block of code
        - We use it to keep from repeating ourselves.

    [X] How to create a function?
        - First: Define => "def"
        - Second: Name your function
        - Use () w/ ":" => ():
        - Use/create a code block under it

    [] Parameters => Place holder value inside the () beside the function
        - Tell Python what to do with the value

    [] Arguments => The values used
        - Tells what the place holder should be when used
    ____________
    [] Scope
    [] Recursion
"""

# greeting = "Hello world"
# print(greeting)

# Define and give it a name 
# def say_hello():
#     #Code Block
#     print("Hello")

# def say_what_I_say(words_to_say):
#     print(words_to_say)

# say_what_I_say("Whooty whoo")
# say_what_I_say("Bye Felicia")

# Create a function that takes 1 parameter
# def Add_ten(number):
    # print(number)
#   -The argument should be an integer
# Add_ten(22)
#   -The function should display the argument plus 10
# Add_ten(22 + 10)

# def add(x, y):
#     print(x + y)

# add(5, 7)

# This function should be passed a list
def place_order(items):

    count = 0
    while count < len(items):
        print(items[count])
        count += 1

my_order = ["Salmon", "Chips", "Spinach"]
place_order(my_order)