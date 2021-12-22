n=int(input())
def distance(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return distance(n-1)+distance(n-2)
for i in range(n):
    num=int(input())
    print(distance(num))