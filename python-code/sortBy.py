def sort_by(arr):
    odd_pos=[]
    even_pos=[]
    for i in range(len(arr)):
        if i%2!=0:
            odd_pos.append(arr[i])
        else:
            even_pos.append(arr[i])
    odd_pos.sort()
    even_pos.sort(reverse=True)
    res=[]
    e,o=0,0
    for i in range(len(arr)):
        if i%2!=0:
            res.append(odd_pos[o])
            o+=1
        else:
            res.append(even_pos[e])
            e+=1
    return res

for _ in range(int(input())):
    size=int(input())
    arr=[int(x) for x in input().split()]
    print(*sort_by(arr))
