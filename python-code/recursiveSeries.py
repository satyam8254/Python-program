def series(n):
    if n==0:
        return (0)
    elif n<=9:
        return n
    elif n%2==0:
        n=n-10
    else:
        n=n-9
    return series(n)
t=int(input())
for i in range(t):
    num=int(input())
    print(series(num))