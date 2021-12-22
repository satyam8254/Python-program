# n=int(input())
# for i in range(n):
#     p=11**i
# print(p)

def pascal(n):
    m=1
    print(m)
    for i in range(1,n+1):
        x=(m*(n-i+1))//i
        print(x)
        m=x
n=int(input())
pascal(n-1)