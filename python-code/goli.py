n=int(input())
for i in range(n):
    b,s,c=map(int,input().split())
    profit=b+s-c
    print(profit)