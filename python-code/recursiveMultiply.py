def multiply(n):
    if n==0:
        return 0
    elif n<10:
        return n
    else:
        p=(n%10)*multiply(n//10)
        return p

t=int(input())
for i in range(t):
    num=int(input())
    num=abs(num)
    print(multiply(num))