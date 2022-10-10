def fib( n):
    if n==0:
        return 0
    elif n<=2:
        return 1
        
    a=1
    b=1
    sum=0
    for i in range(3,n+1):
        sum = a+b
        a=b
        b=sum
    return sum
ans = fib(4)
print(ans)