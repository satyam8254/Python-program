def bestScore(A,B,C):
    # complete the function
    A.sort()
    B.sort()
    C.sort()
    i=j=k=0
    mn=float('inf')
    while i<len(A) and j<len(B) and k<len(C):
        T=sorted([A[i],B[j],C[k]])
        mn=min(mn,abs(T[2]-T[1])+abs(T[0]-T[1]))
        if A[i]==min(T):
            i=i+1
        elif B[j]==min(T):
            j=j+1
        else:
            k=k+1
    print(mn)
#DO not edit anything below this line
# Driver code 
A= [int(x) for x in input().split()] 
B= [int(x) for x in input().split()]  
C= [int(x) for x in input().split()]  
bestScore(A,B,C)