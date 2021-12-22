def reverseSelectionSort(A, n):
    for i in range(n):
        for j in range(i+1,n):
            if A[i]>A[j]:
                A[i],A[j]=A[j],A[i]
                # temp=(A[i])
                # A[i]=A[j]
                # A[j]=temp
    return A[::-1]
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(*reverseSelectionSort(arr, n))