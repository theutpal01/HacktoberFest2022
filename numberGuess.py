"""

NUMBER GUESSING GAME - PYTHON
CREATED BY - UTPAL

"""


from random import randint


def checkers(guess, ans):
	string = ""

	if guess == ans:
		string = "You guessed it correct in"
	
	elif abs(ans - guess) <= 50:
		if guess > ans:
			string = "Little greater than the original answer!"
		else:
			string = "Little smaller than the original answer!"
			
	elif abs(ans - guess) <= 200:
		if guess > ans:
			string = "Greater than the original answer!"
		else:
			string = "Smaller than the original answer!"
		
	elif guess > ans:
		string = "Way greater than the original answer!"
			
	elif guess < ans:
		string = "Way smaller than the original answer!"
	
	return string




num = randint(randint(1, 200), randint(700, 900))
moves = 10
guess = 0


while moves:
	print("You have total moves left =", moves,  "\n")
	guess = int(input("Make a guess (only numbers): "))
	
	string = checkers(guess, num)
	if guess == num:
		print(string, 11- moves, "moves!")
		break
	else:
		print(string)
		moves -= 1
		
		
if guess != num:
	print("You have lost the match!\nOut of the moves.\nThe original answer:", num)
	