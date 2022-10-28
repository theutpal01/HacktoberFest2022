#accept 2 numbers
m=int(input("Enter the first number : "))
n=int(input("Enter the second number : "))

if m > n:
    max=m
    min=n
else:
    max=n
    min=m

while min>0:
    rem=max%min
    max=min
    min=rem


print("The GCD is " + str(max))
