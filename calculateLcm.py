# A simple program to calculate LCM and GCD from input numbers
# By: Anish Shilpakar
# GitHub Username: juju2181

def findGCD(x, y):
    while x != y:
        if x > y:
            x = x - y
        elif x < y:
            y = y - x
    return x


def findLCM(x, y):
    z = x*y
    gcd = findGCD(x, y)
    lcm = int(z/gcd)
    return lcm


x = int(input("n1: "))
y = int(input("n2: "))
print(f'GCD of {x} and {y} : {findGCD(x,y)}')
print(f'LCM of {x} and {y} : {findLCM(x,y)}')
