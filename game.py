import random
print("Rock, Paper, Scissors, Shoot!")
#USER INPUTS
user_choice = input("Please make a selection('rock', 'paper', 'scissors'")
user_choice = user_choice.lower()
print(f"You Chose: {user_choice} ")

#VALIDATE USER INPUTS
valid_options = ["rock", "paper", "scissors"]
if (user_choice not in valid_options):
    print("Not a valid choice, please try again")
    exit()

#COMPUTER SELECTION
computer_choice = random.choice(valid_options)

#DETERMINING THE WINNER
if user_choice == computer_choice:
    print("Tie, go again!")
elif user_choice == scissors:
    if computer_choice == rock
    print("You lose, try again!")
    else:
    print:("You win!")
elif user_choice == "paper":
    if computer_choice == "rock"
    print("You win!")
    else:
    print:("You lose, try again!")
elif user_choice == "rock":
    if computer_choice == "scissors"
    print("You win!")
    else:
    print("You lose, try again")

#DISPLAYING RESULTS
print("Thank you for playing with me!")
#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#
