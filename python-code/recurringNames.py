k=int(input())
s=input().split(" ")
d={}
for j in s:
    if j in d:
        d[j]=d[j]+1
    else:
        d[j]=1
a=[]
for i in d:
    if(d[i]>k):
        a.append(i)
a.sort()
if(len(a)==0):
	print("no such names in this town!!!")
else:
	[print(i) for i in a]























# k=int(input())
# name=list(input().split())
# res=[]
# flag=0
# for i in name:
#     if (i.count(i)>=k):
#         res.append(i)
#         flag=1
# res=sorted(res)
# if flag==0:
#     print("no such names in this town!!!")
# else:
#     for i in range(len(res)):
#         print(i)


