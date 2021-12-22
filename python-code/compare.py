n,q=map(int,input().split())
a=input()
b=input()
queries=[]
for i in range(q):
    queries.append(int(input()))
def check(m):
    s=list(b)
    for i in range(m+1):
        s[queries[i]-1]='1'
    s="".join(s)
    return s>=a
start,end=0,n-1
res=-1
while start<=end:
    mid=(start+end)//2
    if check(mid):
        res=mid
        end=mid-1
    else:
        start=mid+1
ans=['NO']*q
if res!=-1:
    for i in range(res,q):
        ans[i]='YES'
[print(i) for i in ans]
