def longestSubstring(s):
    if len(s)==0:
        return 0
    d={}
    start=0
    maxlength=0
    for i in range(len(s)):
        if s[i] in d and start<=d[s[i]]:
            start=d[s[i]]+1
        else:
            maxlength=max(maxlength,i-start+1)
        d[s[i]]=i
    return(maxlength)

tc=int(input())
for i in range(tc):
    s=input()
    print(longestSubstring(s))

































# def longestSubstring(s):
#     i =0
#     j = 0
#     d={}
#     ans = 0
#     while j < len(s):
#         if s[j] not in d or i>d[s[j]]:
#             ans = max(ans,(j-i+1))
#             d[s[j]] = j
#         else:
#             i = d[s[j]]+1
#             ans = max(ans,(j-i+1))
#             j-=1
#         j+=1
#     return ans
# tc=int(input())
# for i in range(tc):
#     s=input()
#     print(longestSubstring(s))

# s="abcabcbb"
# s1=set(s)
# print(len(s1))