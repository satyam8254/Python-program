n,k=map(int,input().split())
arr=[]
for i in range(n):
    s=input()[:k]
    arr.append(s)
#print(arr)
res=[]
for i in range(k):
    s1=""
    for j in range(n):
        s1=s1+str(arr[j][i])
    res.append(s1)
cnt=0
for i in range(len(res)):
    if sorted(res[i])!=list(res[i]):
        cnt+=1
print(cnt)






















































