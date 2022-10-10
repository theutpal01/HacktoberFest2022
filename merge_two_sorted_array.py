def merge(num1, num2):
    arr3 = [None]*(len(num1)+len(num2))
    i, j, k = 0, 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            k += 1
            i += 1
        else:
            arr3[k] = arr2[j]
            k += 1
            j += 1
            
    while i < len(num1):
        arr3[k] = arr1[i];
        k += 1
        i += 1
        
    while j < len(num2):
        arr3[k] = arr2[j];
        k += 1
        j += 1
    
    return arr3
                
arr1 = [3, 5, 6, 10]
arr2 = [1, 2, 7, 8, 11, 12]
assert merge(arr1, arr2) == [1, 2, 3, 5, 6, 7, 8, 10, 11, 12]
arr1 = [1, 3, 4, 5]
arr2 = [2, 4, 6, 8]
assert merge(arr1, arr2) == [1, 2, 3, 4, 4, 5, 6, 8]
arr1 = [5, 8, 9]
arr2 = [4, 7, 8]
assert merge(arr1, arr2) == [4, 5, 7, 8, 8, 9]
