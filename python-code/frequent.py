def frequent(arr,size):
    dict={}
    for i in range(size):
        if arr[i] in dict:
            dict[arr[i]]+=1
        else:
            dict[arr[i]]=1
    arr.sort(reverse=True)
    arr.sort(key=lambda x:dict[x])
    return arr
for _ in range(int(input())):
    size=int(input())
    arr=[int(x) for x in input().split()]
    print(*frequent(arr,size))

































# def frequent(arr,size):
#     arr.sort()
#     inc_arr=[]
#     dec_arr=[]
#     if len(arr)==1:
#         return arr
#     else:
#         for i in range(size):
#             if arr.count(arr[i])==1:
#                 inc_arr.append(arr[i])
#             else:
#                 dec_arr.append(arr[i])
#         inc_arr.sort(reverse=True)
#         dec_arr.sort(reverse=True)
#         return inc_arr+dec_arr

# for _ in range(int(input())):
#     size=int(input())
#     arr=[int(x) for x in input().split()]
#     print(*frequent(arr,size))