def friends(arr,n,k):
    stack=[]
    for i in range(n):
        while len(stack)!=0 and stack[-1]<arr[i] and k!=0:
            stack.pop()
            k-=1
        stack.append(arr[i])
    return stack
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=[int(x) for x in input().split()]
    print(*friends(arr,n,k))


		