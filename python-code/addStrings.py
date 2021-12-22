# Complete this addStrings() function

def addStrings(num1, num2):     
    ### Here num1 & num2 are strings [Return the addition of these two strings as string]
    num1=num1[::-1]
    num2=num2[::-1]
    res=""
    if len(num2)>len(num1):
        num1,num2=num2,num1
    carry=0
    for i in range(len(num2)):
        temp=int(num1[i])+int(num2[i])+carry
        res=res+str(temp%10)
        carry=temp//10
    for i in range(len(num2),len(num1)):
        temp=int(num1[i])+carry
        res=res+str(temp%10)
        carry=temp//10
    if carry!=0:
        res=res+str(carry)
    return res[::-1]

## Do not change anything below this line:

for _ in range(int(input())):
    n1, n2 = input().split()
    print(addStrings(n1,n2))