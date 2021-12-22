def search(arr, n, elem):
    i = 0
    j = n - 1
    while ( i < n and j >= 0 ):
        if (arr[i][j] == elem ):
            print("Element Found at ", i, ", ", j)
            return 1
        if (arr[i][j] > elem ):
            j -= 1
        else:
            i += 1
    print("Element not found")
    return 0
# Driver Code
arr = [ [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50] ]
search(arr, 4, 29)