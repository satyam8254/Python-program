n=int(input())
arr=[int(x) for x in input().split()]
mn=[]
mx=[]
res=0
for i in range(n):
    res=res+abs(i+1-arr[i])
    mn.append(min(arr[i],i+1))
    mx.append(max(arr[i],i+1))
res=res+2*(abs(max(mn)-min(mx)))
print(res)