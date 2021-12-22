n=int(input())
arr=[int(x) for x in input().split()]
#print(arr)
arr=list(set(arr))
#print(arr)
arr.sort()
#print(arr)
res=arr[:-2]
#print(res)
if len(res)==0:
    print(-1)
else:
    print(*res)