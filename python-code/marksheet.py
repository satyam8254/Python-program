import sys
def jumble(A):
    #Enter your code
    return A

t=int(input())
for i in range(t):  
    n=int(input())
    a=[]
    a=[int(itr) for itr in input().split(" ")]
    jumble(a)
    print(str(n))
    for i in range(n):
        if(i!=0):
            print(" ",end='')
        print(a[i],end='')
    print("\n",end='')