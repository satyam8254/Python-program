def recursivePrint(left,right):
    if left<=right:
        print(left,end=" ")
        left=left+1
        recursivePrint(left,right)

n=int(input())
for i in range(n):
    left,right=map(int,input().split())
    recursivePrint(left,right)