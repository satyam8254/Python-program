def reflection(px,py,qx,qy):
    return (2*qx-px,2*qy-py)
tc=int(input())
for i in range(tc):
    px,py,qx,qy=map(int, input().split())
    print(*reflection(px,py,qx,qy))