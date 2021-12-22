'''n,k = map(int, input().split())
largeQuantityUser = n//k
smallQuantityUser = n%k
result = largeQuantityUser - smallQuantityUser
print(result)'''
n,k = map(int, input().split())
if (n % k == 0):
    print(0)
else:
    print(1)