def contnum(n):
    
    num = 1    # initializing starting number

    for i in range(0, n):     # outer loop to handle number of rows

        for j in range(0, i+1):         # inner loop to handle number of columns
           
            print(num, end=" ")
         
            num = num + 1 # incrementing number at each column
            print("\r")         # ending line after each row

            n = 10
            
            contnum(n)