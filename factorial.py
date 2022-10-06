def f(n):
    if n==0:
        return 1
    return n* f(n-1)
n= int(input("Enter the Number you wanna Find Factorial Of :"))
if(n<0): print("Factorial of negative numbers doesn't exist")
else: print(f(n))