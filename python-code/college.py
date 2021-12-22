def sumofdivisors(n):
    # Code here
    sum=0
    for i in range(1,n+1):
        if n%i==0:
            sum=sum+i
    return sum

n = int(input())
print(sumofdivisors(n))