def index(arr,k):
    n=len(arr)
    start=0
    end=n-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==k:
            return mid
        elif arr[mid]<k:
            start=mid+1
        else:
            end=mid-1
    return end+1
tc=int(input())
for i in range(tc):
    arr=[int(x) for x in input().split()]
    queries=int(input())
    q=[int(x) for x in input().split()]
    for i in range(queries):
        k=q[i]
        print(index(arr,k))