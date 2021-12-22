from collections import Counter
n=int(input())
arr=[int(x) for x in input().split()]
arr.sort()
count=Counter(arr)
flag=1
for i in range(2,arr[-1]+1):
    if count[i]>count[i-1]:
        flag=2
        break
if flag==1:
    res=[]
    for i in range(arr[-1],0,-1):
        temp=[]
        val=count[i]
        if val>0:
            for j in range(1,i+1):
                temp.append(j)
                count[j]=count[j]-val
            for k in range(val):
                res.append(temp)
    print(len(res))
    [print(*i) for i in reversed(res)]
else:
    res=0
    threshold=0
    for i in range(arr[-1],0,-1):
        if count[i]>=threshold:
            threshold=count[i]
        else:
            diff=(threshold-count[i])
            count[i]=count[i]+diff
            res=res+diff
    print(res)

