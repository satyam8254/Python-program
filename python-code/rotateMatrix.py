n=int(input())
arr=[]
for i in range(n):
    a=[int(x) for x in input().split()]
    arr.append(a)
result=[]
for i in range(len(arr[0])):
    arr2=[]
    for j in range(len(arr)):
        arr2.append(arr[j][i])
    result.append(arr2[::-1])
print(len(result))
for i in result:
    print(*i)
    


