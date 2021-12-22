n=int(input())
arr=[str(x) for x in input().split()]
res=0
d={}
for i in arr:
    i=str(''.join(sorted(i)))
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
    res=max(res,d[i])
print(res)