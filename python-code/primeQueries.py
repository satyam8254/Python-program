n,q=map(int,input().split())
prime=[1 for i in range(n+1)]
prime[0],prime[1]=0,0
p=2
while p*p<=n:
    if prime[p]==1:
        for i in range(p*p,n+1,p):
            prime[i]=0
    p+=1
for i in range(1,len(prime)):
    prime[i]+=prime[i-1]
for i in range(q):
    query=int(input())
    print(prime[query])