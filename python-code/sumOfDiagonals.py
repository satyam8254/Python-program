n=int(input())
mtx=[]
for i in range(n):
    l=[int(x) for x in input().split()]
    mtx.append(l)
l1=[]
l2=[]
for i in range(len(mtx)):
    l1.append(mtx[i][i])
#print(l1)
for i in range(len(mtx)-1,-1,-1):
    l2.append(mtx[len(mtx)-1-i][i])
#print(l2)
s1=0
s2=0
for i in range(len(l1)):
    s1=s1+l1[i]
#print(s1)
for i in range(len(l2)):
    s2=s2+l1[i]
#print(s2)
output=s1+s2
print(output)


