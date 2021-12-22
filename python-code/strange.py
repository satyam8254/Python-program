# n = int(input())
# sum = 0
# product = 1
# count = 0
# for i in range(n):
#     num = int(input())
#     remainder = num%10
#     sum = sum+remainder
#     product = product*remainder
#     num = num//10
#     if sum>=product:
#         count=count+1   
# i=i+1 
# print(count)
      
tc=int(input())
cnt=0
for t in range(tc):
    n=int(input())
    s=0
    p=1
    if(n==0):
        cnt=cnt+1
    else:
        while(n>0):
            r=int(n%10)
            s=s+r
            p=p*r
            n=n//10
        if(s>=p):
            cnt=cnt+1
print(cnt)

