tc=int(input())
for i in range(tc):
    n=int(input())
    girl=[int(x) for x in input().split()]
    boy=[int(x) for x in input().split()[:n]]
    girl.sort()
    boy.sort(reverse=True)
    res=[]
    for i in range(n):
        if girl[i] % boy[i] == 0 or boy[i]%girl[i]== 0:
           res.append(1)    
    print(sum(res))


            #print(girl[i],boy[i])