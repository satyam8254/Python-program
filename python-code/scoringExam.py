n,q=map(int,input().split())
time=[int(x) for x in input().split()[:n]]
time.sort(reverse=True)
score=[int(x) for x in input().split()[:n]]
score.sort(reverse=True)
arr=[]
sm=0
for i in range(n):
    sm=sm+time[i]
    arr.append(sm)
for i in range(q):
    ques=int(input())
    print(arr[ques-1])


