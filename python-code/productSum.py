'''num = int(input())
sum = 0
product = 1
while(num>0):
    lastDigit = num % 10
    num = num//10
    sum = sum + lastDigit
    product = product*lastDigit    
result = product-sum
print(result)
'''
'''num = int(input())
sum = 0
product = 1
for i in num:
    sum = sum + int(i)

for i in num:
     product = product * int(i)
result = product - sum
print(result)'''
num = input()
sum = 0
product = 1
for i in num:
    sum = sum + int(i)

for i in num:
     product = product * int(i)
result = product - sum
print(result)
