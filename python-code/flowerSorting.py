def flowerSort(arr,n):
     for i in range(1,n):
          j=i
          while j>0 and arr[j]<arr[j-1]:
               arr[j],arr[j-1]=arr[j-1],arr[j]
               j=j-1
     return arr
n=int(input())
arr=[int(x) for x in input().split()]
print(*(flowerSort(arr,n)))