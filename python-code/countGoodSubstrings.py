def countGoodSubstring(n,string):
    curr=1
    prev=0
    res=0
    for i in range(1,n):
        if string[i]==string[i-1]:
            curr+=1
        else:
            res+=min(curr,prev)
            prev=curr
            curr=1
    return res+min(curr,prev)


n=int(input())
string=input()
countGoodSubstring(n,string)