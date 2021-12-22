from collections import Counter
n=int(input())
arr=list(map(int,input().split()[:n]))
d=Counter(arr)
res=0
for i in d:
    res=res+d[i]//2
print(res)




 



















# n=int(input())
# arr=list(map(int,input().split()[:n]))
# d={}
# for i in arr:
#     if arr[i] in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# cnt=0
# for i in arr:
#     if d[i]%2==0:
#         cnt=cnt+1
# print(cnt)


