def shellshort(z):
    n = len(z)
    gap  = n //2

    while  gap > 0:
        for i in range(gap, n):
            temp = z[i]
            j = i

            while j >= gap and z[j-gap] > temp:
                z[j] = z[j-gap]
                j = j-gap
            z[j] = temp
        gap = gap // 2

z = [5,4,3,1,2,6]

shellshort(z)

print(z)