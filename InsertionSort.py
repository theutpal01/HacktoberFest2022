def insertionSort(a): # Function to implement insertion sort  
    for i in range(1, len(a)):  
        temp = a[i]  
  
        # Move the elements greater than temp to one position   
        #ahead from their current position  
        j = i-1  
        while j >= 0 and temp < a[j] :  
                a[j + 1] = a[j]  
                j = j-1  
        a[j + 1] = temp  
  
def printArr(a): # function to print the array  
  
    for i in range(len(a)):  
        print (a[i], end = " ")  
  
a = [70, 15, 2, 51, 60]  
print("Before sorting array elements are - ")  
printArr(a)  
insertionSort(a)  
print("\nAfter sorting array elements are - ")  
printArr(a)  