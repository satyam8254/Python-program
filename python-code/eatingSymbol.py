'''symbol = str(input(""))
sum = 0
if symbol == str("+"):
    symbol = int(+1)
elif symbol == str("-"):
    symbol = int(-1)
else:
    symbol = int(0)
result = symbol
while(result > 0):
    sum = sum + result
    result = result + 1
print(sum)
'''

'''symbol = input()
sum = 0
while (True):
    if symbol == str("+"):
        sum = sum + 1
    elif symbol == str("-"):
        sum = sum - 1
    else:
        break
print(sum)'''
symbol = input()
sum = 0
for i in symbol:
    if i== "+" :
        sum = sum + 1
    else:
        sum = sum - 1
print(sum)