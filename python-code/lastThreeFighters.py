n=int(input())
if n==1:
    print(0)
elif n==2:
    print(1)
elif n==3:
    print(1)
else:
    power=1
    for i in range(3,n):
        power=power+power
    print(power)

