nameDict={}
sportsDict={}
n=int(input())
for i  in range(n):
    name,sport=input().split()
    if name not in nameDict:
        nameDict[name]=True
        if sport not in sportsDict:
            sportsDict[sport]=1
        else:
            sportsDict[sport]+=1
#print(nameDict)
#print(sportsDict)
maxx=max(sportsDict.values())
for i in sorted(sportsDict.keys()):
    if sportsDict[i]==maxx:
        print(i)
        break    
print(sportsDict['football'] if 'football' in sportsDict else 0)























# n=int(input())
# arr=[]
# for i in range(n):
#     name,sports=input().split()
#     arr.append(sports)
# d={}
# cnt=0
# for i in range(n):
#     if arr[i] in d:
#         cnt=cnt+1
#         if cnt>1:
#             print(arr[i])
# cnt1=0
# for i in range(n):
#     if arr[i]=="football":    
#         cnt1=cnt+1
# print(cnt1)


