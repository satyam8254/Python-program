n=int(input())
arr=[int(x) for x in input().split()[:2*n]]
arr.sort()
sm=0
for i in range(0,2*n,2):
    sm=sm+min(arr[i],arr[i+1])
print(sm)
