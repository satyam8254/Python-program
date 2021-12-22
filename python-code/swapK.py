n,k=map(int,input().split())
arr=[]
arr=list(map(int,input().split()[:n]))
arr[k-1],arr[n-k]=arr[n-k],arr[k-1]
print(*arr)