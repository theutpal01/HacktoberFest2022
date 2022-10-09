def recaman(n=int()):

    l = [0] * n
    l[0] = 0
    print(l[0], end=", ")
    for i in range(1, n):
        rec = l[i - 1] - i
        for j in range(0, i):
            if (l[j] == rec) or rec <= -1:
                rec = l[i - 1] + i
                break
        l[i] = rec
        if i<n-1:
            print(l[i], end=", ")
        else:
            print(l[i])


n = int(input('Enter No. of Terms Required: '))

print()
print('The Recamán\'s Sequence up to the entered no. is: ')

recaman(n)
print('\nThanks For Using:)')
