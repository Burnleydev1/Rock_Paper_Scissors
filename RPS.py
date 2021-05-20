#start
#Code for rock paper scissors

import random

user_wins = 0
comp_wins = 0
draw = 0

def choice():
    user_choice = input("enter either rock, paper or scissors: ")
    if user_choice in ["Rock", "r","R","rock"]:
        user_choice = "r"
    elif user_choice in ["paper", "Paper","p","P"]:
        user_choice = "p"
    elif user_choice in ["scissors","Scissors","s","S"]:
        user_choice = "s"
    else:
        print("invalid input, try again")
        choice()
    return user_choice


def computer_turn():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = "r"
    if comp_choice ==2:
        comp_choice ="p"
    if comp_choice == 3:
        comp_choice ="s"
    return comp_choice

while True:
    print("")
    user_choice = choice()
    comp_choice = computer_turn()
    print("")

    if user_choice == "r":
        if comp_choice == "r":
            print("Computer chose Rock too, It's a tie")
            draw += 1
        elif comp_choice == "p":
            print("Computer chose Paper, you lose")
            comp_wins += 1
        elif comp_choice== "s":
            print("Computer chose Scissors, you win")
            user_wins += 1

    if user_choice == "p":
        if comp_choice == "p":
            print("Computer chose Paper too, It's a tie")
            draw += 1
        elif comp_choice == "s":
            print("Computer chose Scissors, you lose")
            comp_wins += 1
        elif comp_choice== "r":
            print("Computer chose Rock, you win")
            user_wins += 1

    if user_choice == "s":
        if comp_choice == "s":
            print("Computer chose Scissors too, It's a tie")
            draw += 1
        elif comp_choice == "r":
            print("Computer chose Rock, you lose")
            comp_wins += 1
        elif comp_choice== "p":
            print("Computer chose Paper, you win")
            user_wins += 1
    print("")
    print(f"Player Wins: {user_wins}")
    print(f"Computer Wins: {comp_wins}")
    print(f"Ties: {draw}")
    print("")

    play_on = input("Do You Wish To Continue? Y/n: ")
    if play_on in ["Yes","yes","y","Y",""]:
        pass
    elif play_on in ["No","no","N","n"]:
        print("Thanks for Playing 🙂")
        break
    else:
        break
    