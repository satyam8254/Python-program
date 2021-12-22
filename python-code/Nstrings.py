n= int(input())
count=0
for i in range(n):
    string=input()
    if len(string)%2!=0:
        count=count+1
print(count)