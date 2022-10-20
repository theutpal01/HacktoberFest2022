from sys import stdin

def arrayRotateCheck(arr, n):
    #Your code goes here
    for i in range(n-1):
        if (arr[i] > arr[i+1]):
            return (i+1)
    return (0)

def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    print(arrayRotateCheck(arr, n))

    t -= 1