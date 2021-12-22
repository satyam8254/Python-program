size=int(input())
nameDict={}
arr=[]
for i in range(size):
    n=input()
    arr.append(n)
for i in arr[0]:
    c=0
    for j in range(1,len(arr)):
        if(i in arr[j]):
            c+=1
            arr[j]=arr[j].replace(i,"",1)
    if(c==len(arr)-1):
        if i not in nameDict:
            nameDict[i]=1
        else:
            nameDict[i]+=1
for i in sorted (nameDict.keys()) :
    print(i,nameDict[i])