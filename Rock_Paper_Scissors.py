import random
import sys

print('WELCOME TO MY GAME WORLD: ROCK, PAPER, SCISSORS')
# These variables keep track of the number of wins, losses, and ties.
while True:
    computer_count = 0
    player_count = 0
    print('Enter your move: (p)aper, (r)ock, (s)cissors')
    playerMove = input()
    if playerMove == 'quit':
        sys.exit()  # Quit the program.
    if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
        break
    # Display what the player chose.
if playerMove == 'r':
    print('ROCK versus...')
elif playerMove == 'p':
    print('PAPER versus...')
elif playerMove == 's':
    print('SCISSORS versus...')
randomNumber = random.randint(1, 3)
if randomNumber == 1:
    computerMove = 'r'
    print('ROCK')
elif randomNumber == 2:
    computerMove = 'p'
    print('PAPER')
elif randomNumber == 3:
    computerMove = 's'
    print('SCISSORS')
# Display the win,loss or tie
if playerMove == computerMove:
    print('It is a tie!')
elif playerMove == 'r' and computerMove == 's':
    print('Yeey,You win!')
    player_count = player_count + 1
elif playerMove == 'p' and computerMove == 'r':
    print('Okay champ,You win!')
    player_count = player_count + 1
elif playerMove == 's' and computerMove == 'p':
    print('This is your lucky day.You win!')
    player_count = player_count + 1
elif playerMove == 'r' and computerMove == 'p':
    print('The rock has been covered by the paper. Sorry,You lose!')
    computer_count = computer_count + 1
elif playerMove == 'p' and computerMove == 's':
    print('Oops! The paper has been cut by the scissors. You lose!')
    computer_count = computer_count + 1
elif playerMove == 's' and computerMove == 'r':
    print('Damn! The rock has crushed the scissors. You lose!')
    computer_count = computer_count + 1
print("\nSCORE:")
print("User Score:", player_count, "\tComputer Score:", computer_count, "\n")

# FINAL SCORE

print("\n\t\tFINAL SCORE:")
print("User Score:", player_count, "\t\t\tComputer Score:", computer_count, "\n")
if player_count > computer_count:
    print("\n\tCONGRATULATIONS! YOU WON!")
elif player_count < computer_count:
    print("\n\t\tSORRY! YOU LOST!")
else:
    print("\n\t\tOOPS! IT'S A TIE!")
