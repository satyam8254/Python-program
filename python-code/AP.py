def AP(arr,size):
    arr.sort()
    if size>1:
        const=arr[1]-arr[0]
    else:
        return True
    for i in range(size-1):
        if (arr[i+1]-arr[i])!=const:
            return False
    return True
for _ in range(int(input())):
    size=int(input())
    arr=[int(x) for x in input().split()]
    print(AP(arr,size))
