n=int(input())
for i in range(n):
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    if len(l2)>len(l1):
        l1,l2=l2,l1
    c=0
    j=0
    res=[]
    for i in range(len(l1)):
        if (j<len(l2)):
            s=l1[i]+l2[j]+c
        else:
            s=l1[i]+c
        if (s>=10):
            c=s//10
            s=s%10
        else:
            c=0
        j=j+1
        res.append(s)
    if(c>0):
        res.append(c)
    for i in res:
        print(i,end="")
    print()

