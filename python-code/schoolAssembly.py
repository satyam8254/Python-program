n=int(input())
arr=[int(x) for x in input().split()]
res=1
for i in range(1,n):
    if arr[i]<arr[i-1]:
        res+=1
print(res)