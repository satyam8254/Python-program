s=input()
n=int(input())
if len(s)==1 or len(s)==0:
    print(s)
elif len(s)>1:
    if n==0:
        s=s+s[::-1]
    elif n==1:
        s=s+s[len(s)-2::-1]
    print(s)

