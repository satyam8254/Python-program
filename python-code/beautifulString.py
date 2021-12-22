from collections import defaultdict
def beautifulString(s):
    ca,cb,cc=0,0,0
    d=defaultdict(int)
    d[0,0]=1
    res=0
    for i in s:
        if i=='a':
            ca=ca+1
        elif i=='b':
            cb=cb+1
        elif i=='c':
            cc=cc+1
        b=(ca-cb,ca-cc)
        res=res+d[b]
        d[b]=d[b]+1
    return res

n=int(input())
for i in range(n):
    s=input()
    print(beautifulString(s))