n,k=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
res=float('inf')
for i in range(0,n-k+1):
    res=min(res,(arr[i+k-1]-arr[i]))
print(res)