tc=int(input())
for i in range(tc):
    n=int(input())
    size=[]
    eating=[]
    for i in range(n):
        s,e=map(int,input().split())
        size.append(s)
        eating.append(e)
    size.sort()
    eating.sort()
    i=0
    j=0
    mx=1
    while j<n:
        if eating[j]>=size[i]:
            mx=max(mx,j-i)
            i+=1
        else:
            j+=1
    mx=max(mx,j-i)
    print(mx)
