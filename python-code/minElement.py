def minElement(arr,n):
    if n==1:
        return arr[0]
    start=0
    end=n-1
    while start<=end:
        mid=(start+end)//2
        if mid-1>=0 and mid+1<n:
            if arr[mid-1]>=arr[mid]<=arr[mid+1]:
                return arr[mid]
        elif mid-1>=0:
            if arr[mid-1]>=arr[mid]:
                return arr[mid]
        elif mid+1<n:
            if arr[mid]<=arr[mid+1]:
                return arr[mid]
        
        if arr[mid] < arr[end]:
            end=mid-1
        elif arr[mid]>arr[end]:
            start=mid+1
                
n=int(input())
arr=[int(x) for x in input().split()]
print(minElement(arr,n))