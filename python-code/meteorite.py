tc=int(input())
for i in range(tc):
    n,m,q=map(int,input().split())
    x=set()
    y=set()
    for i in range(q):
        Xaxis,Yaxis=map(int,input().split())
        x.add(Xaxis)
        y.add(Yaxis)
    x.add(1)
    y.add(1)
    x.add(n)
    y.add(m)
    region=(len(x)-1)*(len(y)-1)
    xmax=0
    xmin=n
    ymax=0
    ymin=m
    x=list(x)
    y=list(y)
    x.sort()
    y.sort()
    for i in range(len(x)-1):
        xmax=max(xmax,x[i+1]-x[i])
        xmin=min(xmin,x[i+1]-x[i])
    for i in range(len(y)-1):
        ymax=max(ymax,y[i+1]-y[i])
        ymin=min(ymin,y[i+1]-y[i])
    minArea=xmin*ymin
    maxArea=xmax*ymax
    print(region,minArea,maxArea)
