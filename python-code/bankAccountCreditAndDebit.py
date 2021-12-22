# n=int(input())
# balance=0
# for i in range(n):
#     amount=int(input())
#     balance=balance+amount
# print(balance)

class BankAccount:
    def __init__(self):
        self.balance=0
    
    def Balance(self,amount):
        self.balance+=amount
    def result(self):
        print(self.balance)
obj = BankAccount()
n=int(input())
for i in range(n):
    amount=int(input())       
    obj.Balance(amount)
obj.result()








