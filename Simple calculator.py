choice= ("1 = add \n2 = subtract \n3 = divide \n4 = multiply")
print(choice)
operation = int(input("enter your operation number: "))
num1 = int(input("enter your first number: "))
num2 = int(input("enter your second number: "))
if operation == 1:
    print(num1+num2)
    
elif operation == 2:
    print(num1-num2)
    
elif operation == 3:
    print(num1/num2)
    
elif operation == 4:
    print(num1*num2)
    
else:
    print("invalid number try again")
