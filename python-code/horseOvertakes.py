tc= int(input())
pos=[0]*tc
for i in range(tc):
    p,v=map(int,input().split())
    pos[p]=v
d=[0]*11
ovt=0
for i in range(tc):
    vel=pos[i]
    for j in range(vel+1,11):
        ovt=ovt+d[j]
    d[vel]=d[vel]+1
print(ovt)
