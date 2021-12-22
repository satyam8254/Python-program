def sameDiagonal(mtx):
    cnt=0
    for i in range(len(mtx)):
        if mtx[i][0]==mtx[i][1]:
            cnt+=1
    return cnt

t=int(input())
for i in range(t):
    n=int(input())
    mtx=[]
    for i in range(n):
        cell=list(map(int,input().split()))
        mtx.append(cell)
    print(sameDiagonal(mtx))