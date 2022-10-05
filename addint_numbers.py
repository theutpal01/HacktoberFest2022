
# Author: Álvaro Masanori Sato

def verify_numbers(user_input):
    if user_input.strip().isdigit():
        return True
    else:
        return False

def add_numbers(num_1, num_2):
    return (num_1 + num_2)

if(__name__ == "__main__"):
    num_1 = input("Enter the first number: ")
    num_2 = input("Enter the second number: ")

    if(verify_numbers(num_1) and verify_numbers(num_2)):
        print(add_numbers(float(num_1), float(num_2)))
    else:
        print("Please, enter a number!")
    