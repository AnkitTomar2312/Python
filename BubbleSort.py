def BubbleSort(A):
    n = len(A)
    swap = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if A[j] > A[j+1]:
                swap = True
                A[j], A[j+1] = A[j+1], A[j]
        if not swap:
            return

A =  [2, 8, 1, 3, 6, 7, 5, 4] 
BubbleSort(A)

print(A) 