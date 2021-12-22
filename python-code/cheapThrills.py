tc=int(input())
for i in range(tc):
    size=int(input())
    arr=[int(x) for x in input().split()[:size]]
    res=sorted(arr)
    first=set()
    second=set()
    for i in range(0,size,2):
        first.add(arr[i])
        second.add(res[i])
    diff=first-second
    print(len(diff))