n=int(input())
arr=[]
for i in range(n):
    num=int(input())
    arr.append(num)
maxp=[]
for i in range(len(arr)-1):
    p=arr[i]*arr[i+1]
    maxp.append(p)   
print(max(maxp))














# firstLarget=max(arr)
# arr.remove(firstLarget)
# secondLargest=max(arr)
# arr.remove(secondLargest)
# print(firstLarget*secondLargest)