def bubbleSort(arr):
    n = len(arr)
    swap=False

    for i in range(n-1) :
       
        for j in range(n-1) :
            
            if arr[j] > arr[j + 1] : 
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
                swap=True
    
        if not swap:
            break
    
    return arr

arr= [1,2,-3,9,-8,6,0] 
print("Array, Before BubbleSort: ",arr)

result = bubbleSort(arr)

print ("Array, After BubbleSort: ",result)
