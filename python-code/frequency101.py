arraySize,target = map(int, input().split())
occurCount = 0
alist = list(map(int, input().split()))
i = 0
while(i<arraySize):
    if(alist[i]== target):
        occurCount+=1
    i+=1
print(occurCount)