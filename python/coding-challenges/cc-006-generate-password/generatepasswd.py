from random import randint

def validation(entry):
    empty_values=("null", "none", "undefined", "false", "true")
    if entry=="" or entry==None:
        return "Invalid input: FullName can not be empty"
    elif entry in empty_values:
        return f"Your entry cannot be special words like {', '.join(empty_values)}."
    elif not entry.isalpha():
        return f"Your entry {entry} cannot contain number, spaces and other special characthers like *,-,_"
    else:
        return "ok"

def produce_passwd(fullname):
    alpha_count = 3  # number of letters in password
    rand_alphas = ''.join([fullname[randint(0, len(fullname)-1)] for i in range (alpha_count)])
    rand_numbers = str(randint(1000,9999))
    passwd = rand_alphas + rand_numbers
    return passwd

print("Print enter your FullName without spaces and with only with letters. (Exp: JohnDoe, AliceWonder)")
print("For exit the program, please type 'exit'.")
entry = input("Enter FullName: ").strip().lower()
if entry != 'exit':
    while True:
        valid_result = validation(entry)
        if valid_result == "ok":
            print(f"Your password is: {produce_passwd(entry)}")
        else:
            print(valid_result)
        entry = input("Enter FullName('exit' for exiting): ").strip().lower()
        if entry == "exit": break
print("Thank you.")