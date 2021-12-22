def reverseString(s):
    if len(s)==0:
        return s
    else:
        return reverseString(s[1:])+s[0]
n=int(input())
for i in range(n):
    s=input()
    print(reverseString(s))