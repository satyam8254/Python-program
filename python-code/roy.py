def symmetric(mtx,n):
    for i in range(n):
        for j in range(n):
            if int(mtx[i][0][j]) != int(mtx[n-1-i][0][j]):
                return 'NO'
            if int(mtx[i][0][j]) != int(mtx[i][0][n-1-j]):
                return 'NO'
    return 'YES'
t = int(input())
for index in range(t):
    n = int(input())
    mtx = []
    for i in range(n):
        ele = list((input().split()))
        mtx.append(ele)
    print(symmetric(mtx,n))