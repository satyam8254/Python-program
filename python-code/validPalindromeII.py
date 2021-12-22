def validPalindrome(s):
    mismatch=0
    i=0
    j=len(s)-1
    flag=True
    while i<j:
        if s[i]!=s[j]:
            mismatch=mismatch+1
            if mismatch<=1:
                i=i+1
            else:
                flag=False
                break
        else:
            i=i+1
            j=j-1
    mismatch=0
    flag1=True
    while i<j:
        if s[i]!=s[j]:
            mismatch=mismatch+1
            if mismatch<=1:
                j=j-1
            else:
                flag1=False
                break
        else:
            i=i+1
            j=j-1
    if flag==True or flag1==True:
        return True
    else:
        return False
    # return (flag or flag1)
tc=int(input())
for i in range(tc):
    s=input()
    print(validPalindrome(s))

























# def validPalindrome(s):
#     if(s == s[::-1]):
#         return True
#     #for i in range(len(s)):
#     for i in s:
#         s1 = s.replace(i,"")
#         #s1 = str(s[i+1:])+str(s[:i-1])
#         if(s1 == s1[::-1]):
#             return True        
#     return False
# tc=int(input())
# for i in range(tc):
#     s=input()
#     print(validPalindrome(s))






















# tc = int(input())
# for i in range(tc):
#     s = input()
#     flag = False
#     if(s == s[::-1]):
#         flag = True
#     else:
#         for i in range(len(s)):
#             s1 = str(s[i+1:])+str(s[:i-1])
#             if(s1 == s1[::-1]):
#                 flag = True
#                 break
#     if(flag==True):
#         print(True)
#     else:
#         print(False)