def insert(arr,n,x):
    if x<=arr[0]:
       return [x]+arr
    elif x>=arr[len(arr)-1]:
       return arr+[x]
    else:
        for i in range(1,len(arr)):
            if x<=arr[i]:
               return arr[:i]+[x]+arr[i:]
n,x=map(int,input().split())
arr=[]
arr=[int(i) for i in input().split()]
print(*insert(arr,n,x))