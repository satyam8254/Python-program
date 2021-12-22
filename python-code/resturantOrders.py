                                             #time,space
orderNo=int(input())                         #1,1
tableNum=int(input())                        #1,1

res=[0 for i in range(tableNum)]             #n,n

tableNo=[]                                   #1,1
for i in range(orderNo):                     #n,0
    num=int(input())                         #n,1
    tableNo.append(num)                      #n,0

for i in range(orderNo):                     #n,0
    cost=int(input())                        #n,1
    index=tableNo[i]                         #n,1
    res[index-1]=res[index-1]+cost           #n,1

maxCost=max(res)                             #1,1
for i in range(len(res)):                    #n,0
    if res[i]==maxCost:                      #n,0
        print(i+1)                           #n,0


#total time complexity  = 11*n+5=O(n)
#total space complexity = 8+n=O(n)