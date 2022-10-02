# Python program for implementation of Bubble Sort


def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# function for printing array


def printarr(arr):
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")


if __name__ == "__main__":
    arr = []  # Sample Array
    n = int(input("Enter number of elements: "))
    for i in range(n):
        e = int(input("Enter element: "))
        arr.append(e)


print("Original array is: ")
printarr(arr)
bubbleSort(arr)
print("\n")
print("Sorted array is: ")
printarr(arr)
