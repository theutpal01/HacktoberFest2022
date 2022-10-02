# Python Program to create half pyramids for inputted number of rows

print("Creating a half pyramid")
rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")