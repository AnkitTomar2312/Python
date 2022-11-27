def selectionSort(arr,n):
    for index in range(n):
        min_index = index
        for j in range(index+1, n):
            if arr[j] <arr[min_index]:
                min_index = j
        (arr[index], arr[min_index])= (arr[min_index], arr[index])

arr = [2, 8, 1, 3, 6, 7, 5, 4] 
n = len(arr)

selectionSort(arr, n)

print(arr) 