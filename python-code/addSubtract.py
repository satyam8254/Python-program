def addSub(arr,i,target):
    if target==0 and i==len(arr):
        return 1
    if i>=len(arr):
        return 0
    return(addSub(arr,i+1,target)+addSub(arr,i+1,target-arr[i])+ addSub(arr,i+1,target+arr[i]))


target=int(input())
n=int(input())
arr=[int(x) for x in input().split()]
print(addSub(arr,0,target))