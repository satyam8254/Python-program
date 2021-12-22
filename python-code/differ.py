def differ(arr,n):
    count=0
    ans=0
    positive=[0]*(n+1)
    negative=[0]*(n+1)
    positive[0]=1
    for i in range(n):
        if arr[i]%2==0:
            count+=1
        else:
            count-=1
        if count<0:
            ans+=negative[-count]
            negative[-count]+=1
        else:
            ans+=positive[count]
            positive[count]+=1
    return ans

n=int(input())
arr=[int(x) for x in input().split()]
print(differ(arr,n))