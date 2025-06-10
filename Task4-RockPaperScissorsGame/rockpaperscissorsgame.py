# Task 4 - Rock Paper Scissors Game

import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    choice = input("Enter rock, paper, or scissors: ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid input.")
        choice = input("Enter rock, paper, or scissors: ").lower()
    return choice

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Rock, Paper, Scissors Game")
    user = get_user_choice()
    computer = get_computer_choice()
    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")
    result = determine_winner(user, computer)
    print(result)

main()