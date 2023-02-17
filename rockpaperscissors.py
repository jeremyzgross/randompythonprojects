import random

print("Welcome to Rock Paper Scissors")

options = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0


while True:
    user_choice = input("Enter your choice (rock/paper/scissors): ")
    computer_choice = random.choice(options)
    print("The computer chose: ", computer_choice)

    if user_choice not in options:
        print("Invalid input! Please try again.")
        continue

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win! Rock beats scissors.")
        user_score += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win! Paper beats rock.")
        user_score += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win! Scissors beat paper.")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

    print("Your score: ", user_score)
    print("Computer's score: ", computer_score)

    while True:
        play_again = input("Do you want to play again? (y/n) ")
        if play_again.lower() == "y":
            continue
        elif  play_again.lower() == "n":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input! Please enter 'y' or 'n'.")
    break


