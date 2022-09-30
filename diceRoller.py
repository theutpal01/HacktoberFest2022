from random import randint
from time import sleep

over = ""

while True:
	print("Dice is rolling...")
	
	sleep(2)
	number = randint(1, 6)
	
	print("You got a:", number)
	over = input("\nEnter y to exit: ")
	print()
	if over.lower() == "y":
		break