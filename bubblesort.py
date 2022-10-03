#Bubble Sort in python
#Input from the user
arr=list(map(int,input("Enter array:").split()))
print("Array before sorting",arr)
for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        #Comparing consecutive elements
        #If first element is greater than second element,then swapping is done.
        if arr[j]>arr[j+1]:
            #Swapping elements
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("Array after sorting",arr)
#Time Complexity:O(n^2)
#Auxiliary Space:O(1)
