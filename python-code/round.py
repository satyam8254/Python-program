t=int(input())
l1=[]
for i in range(t):
    n=int(input())
    l1.append(list(map(int,input().split()[:n])))
for i in range(0,len(l1)-1):
    round[i]=round(l1[i+1]/l1[i])
    print(round[i])
