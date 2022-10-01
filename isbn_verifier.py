def is_valid(isbn):
    '''Function to check if a given ISNB-10 is valid.'''

    isbn = isbn.replace("-", "")

    if len(isbn) != 10:
        return False

    sum = 0
    if isbn[-1] == "X":
        sum += 10
    else:
        sum += int(isbn[-1])

    if not isbn[:-2].isnumeric():
        return False

    for i in range(len(isbn)-1):
        sum += (int(isbn[i]) * (10-i))

    return sum % 11 == 0
