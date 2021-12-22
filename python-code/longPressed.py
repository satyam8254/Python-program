def longPressed(a,t):
    cnt=0
    res=False
    for i in range(len(t)):
        if cnt<len(a) and a[cnt]==t[i]:
            cnt=cnt+1
        elif i==0 or t[i]!=t[i-1]:
            return res
    if cnt==(len(a)):
        res=True
    return res
tc=int(input())
for i in range(tc):
    actual,typed=input().split()
    print(longPressed(actual,typed))

# a="saeed"
# t="ssaaedd"

# else:
#     flag

# if flag==True:
#     print('True')
# else:
#     print('False')