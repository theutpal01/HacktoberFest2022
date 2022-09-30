


string = "Enter a number: "

num1, num2, num3, num4, num5 = float(input(string)), float(input(string)), float(input(string)), float(input(string)), float(input(string))

maxNum = max(num1, max(num2, max(num3, max(num4, num5))))

print("The greatest number among the given is", maxNum)