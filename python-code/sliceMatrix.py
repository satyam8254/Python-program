row,col=map(int,input().split())
mtx=[]
for i in range(row):
    mtx.append(list(map(int,input().split()[:col])))
l,r,t,b=map(int,input().split())
mtx1=[]
for i in range(t-1,b):
    mtx2=[]
    for j in range(l-1,r):
        mtx2.append(mtx[i][j])
    mtx1.append(mtx2)
for i in range(len(mtx1)):
    print(*mtx1[i])

