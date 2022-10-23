import random

def game(computer, you):
    if computer == you:
        return None
    elif computer == 'sc':
        if you == 'p':
            return False
        elif you == 's':
            return True
    elif computer == 'p':
        if you == 'st':
            return False
        elif you == 'sc':
            return True
    elif computer == 'st':
        if you == 'sc':
            return False
        elif you == 'p':
            return True

print("Computer's turn: stone(st), paper(p), scissors(sc)")
randno= random.randint(1,3)
if randno == 1:
    comp = 'st'
if randno == 2:
    comp = 'p'
if randno == 3:
    comp = 'sc'

you = input("Player's turn: stone(st), paper(p), scissors(sc)\n")
print(f"computer chose  {comp}")
print(f"You chose  {you}")

a= game(comp,you)
if a== None:
    print("The Game is a tie ")
elif a:
    print("yayyyyy!!\n You Won the game")
else:
    print("oppps!!\n You lost the game")
