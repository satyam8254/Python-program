import array
a=array.array("i",[int(x) for x in input().split()])
a1=array.array("i",[int(a[0]) for n in input().split()])
sum = 0
a2=[]
for i in range(a[0]-2):
    sum=sum+a1[i]+a1[i+1]+a1[i+2]
    a2.append(sum)
mn=min(a2)
mx=max(a2)
print(mx,end=" ")
print(mn)

