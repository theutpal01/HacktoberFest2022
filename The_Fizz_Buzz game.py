limit = int(input("Enter the largest number upto which you intend to play FizBuzz"))
print("")
for i in range(1,limit+1):
    if i%3 == 0 and i%5 == 0:
        print("Fizz_Buzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)