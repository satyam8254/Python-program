n = int(input())
givenInt = []
positive = 0
negative = 0
for i in range (0,n):
    num = int(input())
    givenInt.append(num)
    if i%2==0:
        positive=positive+givenInt[i]
    else:
        negative=negative+givenInt[i]
    result=positive-negative
    
print(result)
