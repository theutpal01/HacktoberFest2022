def nseries(n=int(), i=int()):

    if n == 1:
        return 1
    elif n > 1:
        if i == 3:
            return n ** 3 + nseries(n - 1, i)
        elif i == 4:
            return n ** 4 + nseries(n - 1, i)
        elif i == 5:
            return n ** 5 + nseries(n - 1, i)


n = int(input('Enter the No. up to which the series is needed: '))
i = int(input('Enter the Series Index (3/4/5): '))

ans = nseries(n, i)

print()
print('The Required Sum is: ', ans)
print('\nThanks for using:)')
