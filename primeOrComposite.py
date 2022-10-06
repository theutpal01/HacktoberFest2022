n = int(input("Enter a number: "))

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(n, "is a Composite Number.")
            break
    else:
        print(n, "is a Prime Number.")
elif n == 0 or n == 1:
    print(n, "is neither a Prime Number nor a Composite number.")
else:
    print(n, "is a Prime Number.")