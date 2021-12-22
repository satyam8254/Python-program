arr=[int(x) for x in input().split()]
firstSum=0
secSum=0
for i in range(len(arr)):
    if i%2==0:
        firstSum=firstSum+arr[i]
    else:
        secSum=secSum+arr[i]
print(firstSum)
print(secSum)
