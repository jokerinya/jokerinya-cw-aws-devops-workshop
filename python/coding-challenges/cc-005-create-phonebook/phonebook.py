def finding():
    name = input("Find the phone number of :")
    if name in phone_book.keys():
        print(phone_book[name])
    else:
        print(f"Couldn't find phone number of {name}")

def adding():
    name = input("Insert name of the person : ")
    tel = input("Insert phone number of the person: ")
    if tel.isdecimal():
        phone_book[name] = tel
        print(f"Phone number of {name} is inserted into the phonebook")
    else:
        print("Invalid input format, cancelling operation ...")        

def deleting():
    name = input("Whom to delete from phonebook :")
    if name in phone_book.keys():
        del phone_book[name]
    else:
        print(f"Couldn't find phone number of {name}")

def selection_spread(selection):
    if selection == 1: finding()
    if selection == 2: adding()
    if selection == 3: deleting()
    if selection == 4: print("Exiting Phonebook")

print("Welcome to Phonebook APP")
phone_book = {}
selection = None
while selection != 4:
    while phone_book == {}:  # first opening; and phonebook empty
        print("It seems your Phonebook is empty. Let's add some info")
        selection = input("Press 2 for adding new number or press 4 for exiting the program: ").strip()
        if selection.isdecimal() and (int(selection) == 4 or int(selection) == 2):
            selection = int(selection)
            if selection == 4:
                selection_spread(selection)
                break
            if selection == 2:
                selection_spread(selection)
        else:
            print("Invalid entry")
    if selection == 4: break  # check for empty phonebook exit

    selection = input(" 1. Find phone number \n 2. Insert a phone number \n 3. Delete a person from the phonebook \n 4. Terminate \n Select operation on Phonebook App (1/2/3) : ").strip()
    if selection.isdecimal() and (int(selection) in range(1, 5)):
        selection = int(selection)
        selection_spread(selection)