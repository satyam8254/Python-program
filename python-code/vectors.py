a1,a2,a3=map(int,input().split())
b1,b2,b3=map(int,input().split())
perpendicular = a1*b1+a2*b2+a3*b3
#parallel = (a2*b3-a3*b2-(a1*b3-b1*a3)+(a1*b2-a2*b1))
parallel = int( (a2 * b3 - a3 * b2)*(a2 * b3 - a3 * b2)  + (a1 * b3 - b1 * a3)*(a1 * b3 - b1 * a3)  + (a1 * b2 - a2 * b1)*(a1 * b2 - a2 * b1) )
if perpendicular == 0:
    print("2")
elif parallel == 0:
    print("1")
else:
    print("0")