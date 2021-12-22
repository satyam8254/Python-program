n=int(input())
l=[]
for i in range(n):
    num=int(input())
    l.append(num)
l1=[]
for i in range(len(l)):
    if l[i]==0:
        l1.append(l[i])
for  i in range(len(l)):
    if l[i]==1:
        l1.append(l[i])
for i in range(len(l)):
    if l[i]==2:
        l1.append(l[i])
for i in range(len(l1)):
    print(l1[i])
