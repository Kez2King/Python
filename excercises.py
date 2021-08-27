#Start with one coin to start
coins = 1

#Start of loop
gameOn = 0

#Entering into loop
while gameOn == 0:

    #Users options
    print("You have 1 coin")
    print("Yes = 1 \n No = 2")
    question = input("Would you like a coin? 1 or 2 \n")
    Yes = 1
    No = 2
    if question == 1:
        print("You have", coins + 1, "now")
        coins += 1
        #Added something new
        if coins >= 5:
            print("Take some more")
            coins += 5

    # End the loop
    else:
        print("Okay, I'm sorry")
        gameOn += 1