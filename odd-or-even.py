"""Write a function to check if a number if odd or even without
using modulus(%) or dividing (/)"""
def odd_or_even(num):
    odd = True
    for time in range(num +1):
        if odd == True:
            odd = False
        else:
            odd = True
    return odd

if __name__ == "__main__":
    number = int(input("Enter a number to check if its odd or even: ").strip())
    if odd_or_even(number):
        print("Number is odd!")
    else:
        print("Number is even")
