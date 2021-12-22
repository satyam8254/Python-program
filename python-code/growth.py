n = int(input())
sum = 0
for i in range(n):
    num=int(input())
    sum= sum+num
average=sum/n
if average>100:
    print("Excellent!")
else:
    print("Not Excellent!")
