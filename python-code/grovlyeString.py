def GrovlyeString(s):
    s=sorted(s,reverse=True)
    mid=len(s)//2
    res=[""]*len(s)
    res[mid]=s[0]
    left=mid-1
    right=mid+1
    for i in range(1,len(s)):
        if(i%2==0):
            res[left]=s[i]
            left=left-1
        else:
            res[right]=s[i]
            right=right+1
    return "".join(res)
n=int(input())
for i in range(n):
    s=input()
    print(GrovlyeString(s))
































