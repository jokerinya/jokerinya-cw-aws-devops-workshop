from random import randint
objects = [ 'scissors', 'rock', 'paper']
user_point = comp_point = 0

def pointer(winner):
    global user_point, comp_point
    if winner == "user":
        user_point += 1
    else:
        comp_point += 1

def winner_obj(obj1, obj2):
    print(f"User's choice:'{obj1}', Computer's choice: '{obj2}' ")
    if obj1 == obj2: return "tie"
    if obj1 == "paper" and obj2 == "rock":
        return f"{obj1} beats {obj2}"
    if obj1 == "paper" and obj2 == "scissors":
        return f"{obj2} beats {obj1}"
    if obj1 == "scissors" and obj2 == "rock":
        return f"{obj2} beats {obj1}"
    if obj1 == "scissors" and obj2 == "paper":
        return f"{obj1} beats {obj2}"
    if obj1 == "rock" and obj2 == "scissors":
        return f"{obj1} beats {obj2}"
    if obj1 == "rock" and obj2 == "paper":
        return f"{obj2} beats {obj1}"   


def check_status(u):
    user_choice = objects[u]
    computer_choice = objects[randint(0, 2)]
    # describe variables
    obj_winner = winner_obj(user_choice, computer_choice)
    winner = "no one"
    computer = "computer"
    user = "user"
    
    if user_choice == computer_choice: return f"{obj_winner} - {winner} wins\n"
    if user_choice == "rock":
        winner = user if computer_choice == "scissors" else computer
    if user_choice == "scissors":
        winner = user if computer_choice == "paper" else computer
    if user_choice == "paper":
        winner = user if computer_choice == "rock" else computer

    # Score
    pointer(winner)

    return f"{obj_winner} - {winner} wins\n"

selection = 1
print("Please enter your weapon:")
while (user_point < 3) and (comp_point < 3) and selection != 4:
    while True:
        selection = input("1. scissors,\n2. rock,\n3. paper,\n4. exit\n=> ").strip()
        if selection.isdecimal() == True: 
            selection = int(selection)
            if 1 <= selection <= 4: break
        print("Invalid entry.")
    if selection == 4: break
    tur = check_status(selection - 1)
    print(tur)
    print(f"User:{user_point}-Computer:{comp_point}")
if selection == 4:
    print("Exiting Program")
else:
    print(f"User won {user_point} time(s) and computer won {comp_point} time(s)")
    if comp_point > user_point:
        print("Computer has won the game!")
    else:
        print("User has won the game!")