
# Author: Álvaro Masanori Sato

import random

def cpu_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return choices[random.randrange(0, 3)]

def player_choice():
    player = ''

    while(player != 'Rock' and player != 'Paper' and player != 'Scissors'):
        print("You can type 0 for Rock, 1 for Paper and 2 for Scissors")
        print("Or you can type 'r' for Rock, 'p' for Paper and 's' for Scissors")
        player = input("Choose [Rock, Paper, Scissors]: ")

        player = player.lower()

        if(player == '0' or player == 'r' or player == 'rock'):
            player = 'Rock'
        elif(player == '1' or player == 'p' or player == 'paper'):
            player = 'Paper'
        elif(player == '2' or player == 's' or player == 'scissors'):
            player = 'Scissors'
    return player

def verify_winner(cpu, player):
    # Rock -> Scissor
    # Paper -> Rock
    # Scissor -> Paper

    print(f"\n\nCPU -> {cpu} | Player -> {player}")

    if(cpu == player):
        print("Tie")
    elif((cpu == 'Rock' and player == 'Paper') or (cpu == 'Paper' and player == 'Scissors') or (cpu == 'Scissors' and player == 'Rock')):
        print("Player is the Winner")
    else:
        print("CPU is the Winner")

if(__name__ == "__main__"):
    cpu = cpu_choice()
    player = player_choice()
    result = verify_winner(cpu, player)