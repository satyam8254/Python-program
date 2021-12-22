def countRotations(arr):
    n = len(arr)
    start = 0
    end = n-1
    while start<=end:
        mid = start+(end-start)//2
        prev = (mid-1+n)%n
        next = (mid+1)%n
        if arr[mid]<arr[prev] and arr[mid]<=arr[next]: return mid
        elif arr[mid]<arr[start]: end = mid-1
        elif arr[mid]>arr[end]: start = mid+1
        else: return 0
# Driver code
arr = [1,1,2,3,4,5]
n = len(arr)
print(countRotations(arr))