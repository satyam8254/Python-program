def get(num):
    ret=0
    while(num!=0):
        ret+=num//5
        num=num//5
    return ret

tc=int(input())
for i in range(tc):
    n=int(input())
    low=0
    high=10**18
    res=high
    while(low<=high):
        mid=(low+high)//2
        val=get(mid)
        if val>=n:
            high=mid-1
            res=min(res,mid)
        else:
            low=mid+1
    print(res)
