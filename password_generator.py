import random
print("Welcome to your Password Generator")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"

number = input("Number of passwords? ")
number = int(number)

length = input("Password length? ")
length = int(length)

print("\nHere are your passwords: ")

for pwd in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)