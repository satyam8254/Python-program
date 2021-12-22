def changeQueries(leftIndex,rightIndex,value,arr_size):
    arr=[0]*arr_size
    for index in range(leftIndex,rightIndex+1):
        arr[index]=arr[index]+value
    return arr

arr_size,No_queries=map(int,input().split())
for queries in range(No_queries):
    leftIndex,rightIndex,value=map(int,input().split())
    print(*changeQueries(leftIndex,rightIndex,value,arr_size))
