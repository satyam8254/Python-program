n=int(input())
l1=[]
for i in range(n):
    num=int(input())
    l1.append(abs(num))
l2=[]
for i in range(len(l1)):
    sq=l1[i]**2
    l2.append(sq)
res=sorted(l2)
for i in range(len(res)):
    print(res[i])
