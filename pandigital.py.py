# python program to check whether a number is pandigital or not
# example - 10243. contains all digits from 0-4
# NOTE - 01234 is equal to 1234, leading zeroes are not considered

import math

def calculate_digits(x) :
    return int(math.log(x, 10)) + 1
    
def isPandigital(x) :
    no_of_digits = calculate_digits(x)
    x = str(x)
    to_array = [char for char in x]
    to_array.sort()
    copy = ''
    for i in range(no_of_digits) :
        copy += str(i)
    to_array_copy = [char for char in copy]
    return to_array_copy == to_array

n = int(input())
print(isPandigital(n))