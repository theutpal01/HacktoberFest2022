n = int(input("Enter your number: "))    
factorial = 1    
if n < 0:    
   print(" Factorial doesn't exist for negative numbers !!")    
elif n == 0:    
   print("Factorial of 0 = 1")    
else:    
   for i in range(1,n + 1):    
       factorial = factorial * i    
   print("Factorial of",n,"is :",factorial)