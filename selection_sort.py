def Selection_Sort(array):
    for i in range(0, len(array) - 1):
        smallest = i
        for j in range(i + 1, len(array)):
            if array[j] < array[smallest]:
                smallest = j
        array[i], array[smallest] = array[smallest], array[i]

array = input('Enter the list of numbers: ').split()
array = [int(x) for x in array]
Selection_Sort(array)
print('List after sorting is : ', array)
