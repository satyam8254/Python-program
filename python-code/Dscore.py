def D_Score(arr,d,n):
    penality=[]
    for i in range(n):
        for j in range(d+1):
            if j==d+1:
                penality.append(arr[j])
    #return min(penality)
    return penality

for _ in range(int(input())):
    n,d=map(int,input().split())
    arr=[int(x) for x in input().split()]
    print(D_Score(arr,d,n))
