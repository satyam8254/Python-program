#Distance(arr[i],arr[j]) = (i x arr[i]-j x arr[j]) - (arr[i]+arr[j])
n=int(input())
arr=[int(x) for x in input().split()[:n]]
first=[]
second=[]
for i in range(len(arr)):
    first.append((i-1)*arr[i])
    second.append((i+1)*arr[i])    
print(max(first)-min(second))   



















