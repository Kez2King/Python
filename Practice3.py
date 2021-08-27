# Make a wallet containing $100
wallet = 100

# Make a menu: four items
menu = ("Steak: 39.99", " Salmon: 29.99", "Pasta: 25.99", "Pizza: 12.99")
print("Here is the menu", menu)

# Start a Loop
order = 0
while order == 0:
    Steak = {
        "Price": 39.99
    }
    Salmon = {
        "Price": 29.99
    }
    Pasta = {
        "Price": 25.99
    }
    Pizza = {
        "Price": 12.99
    }
# Ask user for input
    users_choice = input ("What would you like to eat? ")

        #Create options
        # Display remaining balance in wallet
    # if 24.99 < wallet < 100:
    #     order_again = input("Would you like to order again? 1: Yes or 2: No")
    #     if order_again == 1:
    #         print("Ok")
    if users_choice == Steak:
        print("You have", wallet - Steak["Price"], "left.")
        wallet -= Steak["Price"]

    elif users_choice == Salmon:
        print("You have", wallet - Salmon["Price"], "left.")
        wallet -= Salmon["Price"]

    elif users_choice == Pasta:
        print("You have", wallet - Pasta["Price"], "left.")
        wallet -= Pasta["Price"]

    elif users_choice == Pizza:
        print("You have", wallet - Pizza["Price"], "left.")
        wallet -= Pizza["Price"]
    else:
        print("Sorry, we don't have that option.")

    if 24.99 < wallet < 100:
            order_again = input("Would you like to order again? 1: Yes or 2: No \n")
            if order_again == 1:
                print("Ok")
            else:
                order = 1
                print("Have a wonderful day")
    if wallet < 24.99:
        # print("That's it for you. Enjoy your meal.")
        # break
        warning_trail = input("Your getting too low, Would you like to test your luck? 1: Yes or 2: No \n")
        Yes = 1
        No = 2
        if warning_trail == 1:
            import random
            cpu_wheel = random.randint(1,2)
            print("You have a 50-50 chance to win, 1 is your lucky number, but 2 will destroy you.")
            print("Your number is,")
            print(cpu_wheel)
            if cpu_wheel == 1:
                print("You win $10,000.")
                break
            else:
                print("You lose. Your coming with me.")
                print("Now, you are in a pothole.")
                stray_dog = input("Now, you meet a stray dog, would you like to adapt him? 1: Yes or 2: No")
                if stray_dog == 1:
                    print("Congradulation, the dog was the CEO of Amazon and grants you 1 billion dollars. \n")
                    print("Now, you go back to the resturant to shut them down for kicking you out. \nCongradulations")
                    break
                else:
                    print("PETA gives you grief")
                    break
        else:
            print("Alright, Have a wonderful day.")
            order += 1