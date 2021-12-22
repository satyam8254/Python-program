n= int(input())
even=0
odd=0
for i in range(1,n+1):
    num = int(input())
    if num%2==0:
        even=even+1
    elif num%2!=0:
        odd=odd+1
print(odd)
print(even)

