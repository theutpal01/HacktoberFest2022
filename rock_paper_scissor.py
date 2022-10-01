# rock -> scissor
# scissor -> paper
# paper -> rock

import random

def game(comp, you):
    if comp==you:
        return None
    elif ((comp == "r" and you == "s")or(comp == "s" and you == "p")or(comp == "p" and you == "r")):
        return False
    else:
        return True


while(1):
    r = random.randint(1,3)

    if (r == 1):
        comp = "r"
    elif (r == 2):
        comp = "p"
    elif (r == 3):
        comp = "s"

    print("Enter r for Rock, p for Paper and s for Scissor")
    you = input()

    result = game(comp,you)

    if (result == None):
        print(f"Game is tie.\nComputer choose {comp} and you choose {you}")
    elif (result == True):
        print(f"Congratulations! You are winner.\nComputer choose {comp} and you choose {you}")
    elif (result == False):
        print(f"You lose. Computer wins.\nComputer choose {comp} and you choose {you}")

    print("Do you want to play again?(y/n)")
    choice = input()
    if choice == 'y':
        continue
    elif choice == 'n':
        print("Thanks for visiting")
        break
