# Create the different entries for the different individuals

names = {}
 
def myPhoneBook():
    # List the options for the user
    print(" 1. Look up entry",
     "\n 2. Set an Entry",
     "\n 3. Delete an entry",
     "\n 4. List all entries",
     "\n 5. Quit")

    # Starting Loop
    start = 0
    while(start == 0):

        # Identifies that the input in an integer
        response = int(input("What to do? Select 1 - 5 \n"))
        if(response == 1):
            # Response to an Empty PhoneBook
            if(names == {}):
                print("There are no entries at this time, Please add contacts.")
            else:
                name_check = input("Who are you looking for? \n")
                name_search = map(lambda x : name_check, names)
                result = list(name_search)[0]
                # Looks through the dictionary to get a name
                if(name_check == result):
                    print(name_check, ":", names.get(name_check))
                else:
                    print("Name is not here.")

        elif(response == 2):
            contact_name = input("Enter Name: ")
            contact_number = input("What's your number? ")
            names.update({contact_name: contact_number})
            print("Contacts Updated")

        elif(response == 3):
            if(names == {}):
                print("No Contacts to delete")
            else: 
                name_delete = input("What to remove?\n")
                name_search = map(lambda x : name_delete, names)
                result = list(name_search)[0]
                if(name_delete == result):
                    names.pop(name_delete)
                    print("Removed Successfully")
                else:
                    print("There is no such name")

        elif(response == 4):
            if(names == {}):
                print("You dont have any contacts.")
            else:
                for key, value in names.items():
                    print(key, ":", value)

        elif(response == 5):
            print("Thank you")
            start = 1
        else:
            print("Not an option")

myPhoneBook()