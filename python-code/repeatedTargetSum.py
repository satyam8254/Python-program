def repeatedSum(arr,n,k,i):
    if k==0:
        return 1
    if k<0 or i==n:
        return 0
    return repeatedSum(arr,n,k-arr[i],i)+repeatedSum(arr,n,k,i+1)
n,k=map(int,input().split())
arr=list(map(int,input().split()))
print(repeatedSum(arr,n,k,0))