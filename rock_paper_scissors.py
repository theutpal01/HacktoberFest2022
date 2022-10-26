import random

user_input = input("Enter a choice (rock, paper, scissors): ")
sample_space = ["rock", "paper", "scissors"]
computer_action = random.choice(sample_space)
print(f"\nYou chose {user_input}, computer chose {computer_action}.\n")

if user_input == computer_action:
    print(f"Both players selected {user_input}. It's a tie!")
elif user_input == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_input == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_input == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")