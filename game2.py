import random


print("WELCOME TO OUR ROCK PAPER SCISSORS GAME")


#USER INPUTS


user_choice = input("Please make a selection('rock', 'paper', 'scissors'): ") 
user_choice = user_choice.lower()
print("You chose:", user_choice)
print(f"You chose: '{user_choice}' ")


#VALIDATE USER INPUTS
valid_options = ["rock", "paper", "scissors"]

#breakpoint()

if user_choice in valid_options:
    pass
else:
    print("OOPS INVALID TRY AGAIN")
    exit() #quit()


#COMPUTER CHOICE


#Import Random


computer_choice = random.choice(valid_options)
print(f"Computer chose: '{computer_choice}' ")


#This code was adapted from code shared in slack by Bonnie Auger
#DETERMINE THE WINNER
if user_choice == computer_choice:
    print("It is a tie, please try again!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("You win!")
    else:
        print("You lose!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win!")
    else:
        print("You lose!")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("You win!")
    else:
        print("You lose!")
#DISPLAY RESULTS
print("Thanks for playing. Please play again!")


#-------------------
#Welcome 'Player One' to my Rock-Paper-Scissors game...
#-------------------
#Please choose either 'rock', 'paper', or 'scissors': rock
#You chose: 'rock'
#The computer chose: 'paper'
#-------------------
#Oh, the computer won. It's ok.
#-------------------
#Thanks for playing. Please play again!