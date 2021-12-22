t=int(input())
for i in range(t):
    matrix=[]
    r,c=map(int,input().split())
    for j in range(r):
        matrix.append(map(int,input().split()[:c]))
    print(matrix)

