import random

def getDigits(num):
	return [int(i) for i in str(num)]
	
def noDuplicates(num):
	num_li = getDigits(num)
	if len(num_li) == len(set(num_li)):
		return True
	else:
		return False

def generateNum():
	while True:
		num = random.randint(1000,9999)
		if noDuplicates(num):
			return num

def numOfBullsCows(num,guess):
	bull_cow = [0,0]
	num_li = getDigits(num)
	guess_li = getDigits(guess)
	
	for i,j in zip(num_li,guess_li):
		if j in num_li:
			if j == i:
				bull_cow[0] += 1
		
			else:
				bull_cow[1] += 1
				
	return bull_cow

num = generateNum()
tries =int(input('Enter number of tries: '))

while tries > 0:
	guess = int(input("Enter your guess: "))
	
	if not noDuplicates(guess):
		print("Number should not have repeated digits. Try again.")
		continue
	if guess < 1000 or guess > 9999:
		print("Enter 4 digit number only. Try again.")
		continue
	
	bull_cow = numOfBullsCows(num,guess)
	print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
	tries -=1
	
	if bull_cow[0] == 4:
		print("You guessed right!")
		break
else:
	print(f"You ran out of tries. Number was {num}")
