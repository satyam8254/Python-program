n,k=map(int,input().split())
list1=list(map(int,input().split()[:n]))
b=int(input())
list1.remove(list1[k])
sm=sum(list1)
splitedBill=sm//2
charged=b-splitedBill
if charged==0:
    print("It is Correct!")
else:
    print(charged)