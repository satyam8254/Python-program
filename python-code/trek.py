def trek(step,level):
    cnt=0
    valley=0
    for i in range(step):
        if(level[i]=='U'):
            cnt+=1
            if(cnt==0):
                valley+=1
        else:
            cnt-=1
    return valley
n=int(input())
for i in range(n):
    step=int(input())
    level=input()
    print(trek(step,level))