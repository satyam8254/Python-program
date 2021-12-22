n=int(input())
for i in range(n):
    instruction=input()
OFF=0
ON=1
for i in range(n):
    if instruction[i]=='TOGGLE' and instruction[i+1]=='TOGGLE':
        result=OFF
    elif instruction=='OFF':
        result=OFF
    elif instruction=='ON':
        result=ON
print(result)

