import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if player == 0:
  print(rock)
elif player == 1:
  print(paper)
elif player == 2:
  print(scissors)
else:
  print("Invalid number!, You lose!")
comp=random.randint(0,2)
if comp == 0:
  print(rock)
elif comp == 1:
  print(paper)
else:
  print(scissors)
game=[player,comp]
if (game[0]==0 and game[1]==2) or (game[0]==1 and game[1]==0) or (game[0]==2 and game[1]==1):
  print("You win!")
elif (game[0]==0 and game[1]==0) or (game[0]==1 and game[1]==1) or (game[0]==2 and game[1]==2):
  print("Draw!")
else:
  print("You lose!")