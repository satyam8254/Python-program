string=input().split()
mx=len(string[0])
for i in range(len(string)):
    if len(string[i])>mx:
        mx=len(string[i])
print(mx)