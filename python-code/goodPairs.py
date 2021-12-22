# import array
# arr=array.array("i",[])
# num=int(input().split())
# arr.append(num)
# print(arr)

list1=list(map(int,input().split()))
cnt=0
for i in range(len(list1)):
    for j in range(len(list1)):
        if list1[i]==list1[j] and i<j:
            cnt=cnt+1
print(cnt)