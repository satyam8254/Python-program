tc=int(input())
for i in range(tc):
    l=list(map(int,input().split()))
    l.sort()
    one=(l[1]-l[0])//2
    l[1]=l[1]-2*one
    two=(l[2]-l[1])//2
    l[2]=l[2]-2*two
    print(l[2]+one+two)