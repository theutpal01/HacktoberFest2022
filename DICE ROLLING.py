import random


count = 0
dice_faces = [1, 2, 3, 4, 5, 6]
you = 0
PC = 0

def play():

    user_shakes()
    game()


def user_shakes():

    shakes = int(input("Enter the how many times you want to shake (max is 3) : ")) # int is necessery

    if shakes == 1:
        a1 = random.choice(dice_faces[::3])
        return (a1)

    elif shakes == 2:
        a2 = random.choice(dice_faces[1:4])
        return (a2)

    elif shakes == 3:
        a3 = random.choice(dice_faces[2:5])
        return (a3)

    else:
        print("Enter a valid input")

def game():

    b = int(random.choice(dice_faces))    # int is necessary
    c = int(user_shakes()) # get the return value from def user shakes

    if b == c:
        print("Tied the round!")

    if check_winner(b, c):
        print("PC won the round")
        PC_win()

    elif check_winner(c,b):
        print(str(user)+" won the round")
        user_win()

def check_winner(x,y):
    if(x>y):
        return True

def PC_win():
    global PC
    PC=+1

def user_win():
    global you
    you +=1

def increment():
    global count
    count += 1

def final_result(X,Y):
    if X > Y :
        print( str(user)+" won the game")
    elif X < Y :
        print("PC won the game")
    else:
        print("Tied game")


def run():
    global user # this is necessery to use this variable in another functions
    user = input("Enter the player name : ")
    print("OK let's Play " + user.upper())

    while count < 5:
        print(play())
        increment()

    else:
        print(final_result(you,PC))



print(run())










