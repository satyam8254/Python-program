def hackMoney(n):
    if n==0:
        return False
    if n==1:
        return True
    if n%10==0 and n%20==0:
        return hackMoney(n//10) or hackMoney(n//20)
    elif n%10==0:
        return hackMoney(n//10)
    elif n%20==0:
        return hackMoney(n//20)
    else:
        return False
n= int(input())
for i in range(n):
    num=int(input())
    if hackMoney(num)==True:
        print("Yes")
    else:
        print("No")
    