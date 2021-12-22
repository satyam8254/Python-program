def anagram(s,t):
    s1=len(s)
    s2=len(t)
    if s1!=s2:
        return False
    s=sorted(s)
    t=sorted(t)
    for i in range(s1):
        if s[i]!=t[i]:
            return False
    return True
tc=int(input())
for i in range(tc):
    arr=list(input().split())
    print(anagram(arr[0],arr[1]))