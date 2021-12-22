def compress(st):
    ### Complete this function.
    i=0
    compressed=""
    while i!=len(st):
        cnt=1
        while i<len(st)-1 and st[i]==st[i+1]:
            cnt=cnt+1
            i=i+1
        if cnt==1:
            compressed=compressed+str(st[i])
        else:
            compressed=compressed+str(st[i])+str(cnt)
        i=i+1
    print(compressed)
    
t = int(input())
for _ in range(t):
    st = input()
    compress(st)