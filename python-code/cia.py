arr=[]
for _ in range(int(input())):
    arr.append(int(input()))
maxRecord=1
dict={}
for i in arr:
    if i in dict:
        dict[i]+=1
        maxRecord=max(maxRecord,dict[i])
    else:
        dict[i]=1
res=0
for key,value in dict.items():
    if dict[key]==maxRecord:
        res=max(res,key)
print(res) 
