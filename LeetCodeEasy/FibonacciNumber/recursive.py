
def fib( n):
    if n==0:
        return 0
    elif n<=2:
        return 1
    return (fib(n-1)+fib(n-2))
print(fib(5))