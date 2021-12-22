def gameOfDeath(n,k):
    if n==1:
        return 1
    else:
        return (gameOfDeath(n - 1, k) + k-1) % n + 1
tc=int(input())
for i in range(tc):
    n,k=map(int,input().split())
    print(gameOfDeath(n,k))
    