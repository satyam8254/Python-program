def palindrome(s):
    if len(s)<1:
        return True
    else:
        if s[0]==s[-1]:
            return palindrome(s[1:-1])
        else:
            return False
    
n=int(input())
for i in range(n):
    s=input()
    print(palindrome(s))