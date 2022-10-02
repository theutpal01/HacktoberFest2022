#NUMBER GUESS GAME
import random
number=random.randint(1,100)
print("Welcome to the GUESS GAME")
print('''
Rules:-
1.You can guess a number between 1 to 100
2.You have only 10 trials or else the game will be over
3.Any other input rather than what is adviced may pop up error
''')
trial = 0
while True:
    trial =trial+1
    userinp=int(input("Enter the Number\n"))
    if userinp != number and trial !=10:
        print("Try again!!\nYou have only",10-trial,"trials left")
        if userinp>number:
            print("The number you enterd is greater than the actual number")
        elif userinp<number:
            print("The number you entered is smaller than the actual number")

        continue         
    elif userinp == number and trial != 10:
        print("Congratulations you have entered the correct number in",trial,"trials")
        break
    elif trial == 10:
        print("Game over")
        break
    else:
        print("Please enter correct values as per the rule")
        break