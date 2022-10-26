import random
import math

lower = int(input("enter the lower limit: "))
upper = int(input("enter the upper limit: "))

x = random.randint(lower,upper)
print("\n\tYou've only ",round(math.log(upper-lower + 1,2)),"chances to guess the number!\n")

count = 0

while count<math.log(upper-lower+1,2):
    count += 1
    guess = int(input("Guess a number: "))

    if x==guess:
        print("Congratulations! You did it in",count,"try")
        break
    elif x>guess:
        print("You guessed too small")
    elif x<guess:
        print("You guessed too big")

if count>= math.log(upper-lower+1,2):
    print("The number is %d"%x)
    print("\nBetter luck next time")
