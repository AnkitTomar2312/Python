def InsertionSort(A, n):
    for i in range(1, n):
        key = A[i]
        j = i-1
        while j >=0 and key < A[j]:
            A[j+1] = A[j]
            j -=1
        A[j+1] = key

A =  [2, 8, 1, 3, 6, 7, 5, 4]
n = len(A)
InsertionSort(A, n)
print(A)  