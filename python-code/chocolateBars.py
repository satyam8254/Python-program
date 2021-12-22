from collections import defaultdict
import math
def factor(n):
    cnt=0
    for i in range(1,1+int(math.sqrt(n))):
        if n%i==0:
            cnt=cnt+1
            if n//i!=i:
                cnt=cnt+1
    return cnt
def pair(arr,n):
    d=defaultdict(int)
    for i in arr:
        x=factor(i)
        d[x]=d[x]+1
    res=0
    for x in d:
        res+=(d[x]*(d[x]-1))//2
    return res   

n=int(input())
arr=map(int,input().split())
print(pair(arr,n))






















# n=int(input())
# l1=[int(x) for x in input().split()[:n]]
# l2=[]
# for i in l1:
#     cnt=0
#     for j in range(1,i+1):
#         if i%j==0:
#             cnt+=1
#     l2.append(cnt)
# l3=[]
# for i in range(len(l2)):
#     if l2.count(i)>1:
#         l3.append(i)
# cnt1=0
# for i in range(len(l2)):
#     if l3 in l2:
#         cnt1+=1
# print(cnt)



