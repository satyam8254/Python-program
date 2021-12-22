def find_k(l, k):
    # Implement this and return YES if found else return No
    low=0
    high=len(l)-1
    mid=0
    while low<=high:
        mid=(high+low)//2
        if l[mid]<k:
            low=mid+1
        elif l[mid]>k:
            high=mid-1
        else:
            return "YES"
    return "NO"
    
from sys import stdin
N,Q = input().split()
a = list(map(int,input().split(' ')))
a.sort() 
for i in range(int(Q)):
    k = int(input())
    print(find_k(a, k))


    # for i in l:
    #     if k in l:
    #         return ("YES")
    #     return "NO"