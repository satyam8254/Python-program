n=int(input())
stock=[]
for i in range(n):
    price=int(input())
    stock.append(price)
profit=0
if len(stock)==1:
    print(0)
else:
    if stock[0]>stock[1]:
        mn=stock[1]
        for i in range(2,len(stock)):
            if stock[i]<mn:
                mn=stock[i]
            else:
                earn=stock[i]-mn
                if earn>profit:
                    profit=max(profit,earn)
    if stock[0]<stock[1]:
        mn1=stock[0]
        for i in range(1,len(stock)):
            if stock[i]<mn1:
                mn1=stock[i]
            else:
                earn1=stock[i]-mn1
                if earn1>profit:
                    profit=max(profit,earn1)
    print(profit)






















# n=int(input())
# stock=[]
# for i in range(n):
#     price=int(input())
#     stock.append(price)
















