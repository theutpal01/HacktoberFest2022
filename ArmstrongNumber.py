x = input("Enter your number to check if it is a Armstrong number or not: ")
l = len(x)
test = int(x)
sum = 0
while (test > 0):
    rem = test % 10
    sum += rem**l
    test //= 10
if sum == int(x):
    print("The number is a Armstrong number!!")
else:
    print("The number is a not Armstrong number!!")
