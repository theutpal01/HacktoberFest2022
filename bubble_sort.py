def bubble_sort(arr):

    iterations=0
    for i in range(len(arr)):
        for j in range(len(arr)-(i+1)):
            iterations+=1
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    
    return arr,iterations


arr=[8,5,3,8,9,10,34,56]
print(bubble_sort(arr))