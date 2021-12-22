n1=int(input())
n2=int(input())
a1=list(map(int,input().split()[:n1]))
a2=list(map(int,input().split()[:n2]))
l1=[]
l2=[]
for i in range(len(a1)):
    if a1[i]<0:
        a1[i]=abs(a1[i])
        l1.append(a1[i])
    else:
        l1.append(a1[i])
#print(l1)
for i in range(len(a2)):
    if a2[i]<0:
        a2[i]=abs(a2[i])
        l2.append(a2[i])
    else:
        l2.append(a2[i])
#print(l2)
num1=max(l1)
num2=max(l2)
p=num1*num2
print(p)