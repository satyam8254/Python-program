n=int(input())
arr=[]
for i in range(n):
    num=int(input())
    arr.append(num)
firstLarget=max(arr)
arr.remove(firstLarget)
secondLargest=max(arr)
arr.remove(secondLargest)
thirdLargest=max(arr)
print(firstLarget*secondLargest*thirdLargest)

#time complexity = O(n)
#space complexity =O(1)