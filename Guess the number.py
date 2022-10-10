import random

life = 0

y = int(input("greater than = "))
x = int(input("less than = "))

def game():
 def guess(z):

    random_number = random.randint(y, z)  # z is the parameter
    guess = 0 #this will not allow to random number = 0 ,while the guess is aleady 0 while loop won't continuew
    while (guess != random_number) and (life < 3):  # this loop continue under this function
        guess = int(input(f"Guess the number between {y} and {x}: "))

        if guess < random_number:
            print("guess too low")
            health()


        elif guess > random_number:
         print("sorry guess is too  high")
         health()

        if guess == random_number:
            print("you won")

    else:
        print("you lost")




 guess(x) # the bottem z<x this is the way

def health():
    global life
    life += 1

def play():
    while (life < 3) :
        print(game())
    else:
        print("Game over")

print(play(),)





