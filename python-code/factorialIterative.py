n= int(input())
if n==0:
    print(1)
elif n<0:
    print("undefined")
else:
    f=1
    for i in range(1,n+1):
        f=f*i
    print(f)
