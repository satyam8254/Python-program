import math
n=int(input())
income=[]
children=[]
count=0
sum = 0  
for i in range(n):
    num1=int(input())
    income.append(num1)
for i in range(n):
    num2=int(input())
    children.append(num2)
    if children[i]>2:
        sum=sum+income[i]
        count=count+1
if count==0:
    print(-1)
else:
    print(math.floor(sum/count))

# time complexity = O(n)
# space complexity = O(n)