n=int(input()) #c1
arr=[]
count=0
for i in range(n): #n
    num= int(input()) #c2
    arr.append(num) #c3
q=int(input()) #c4
for i in range(len(arr)): #n
    if arr[i] == q:
        count=count+1 #c5
print(count) #c6


# line1-->c1(1)
# line4-->O(n)
# line5-->c2*(n)
# line6-->c3*(n)
# line7-->c5(1)
# line8-->O(n)
# line10-->c5*(n)
# line11-->c6(1)
# O(1)+O(n)+(c2*n)+(c3*n)+O(1)+O(n)+(c5*n)+O(n) constant will remove
# O(n)+O(n)+O(n)+O(n)+O(n)+O(n)-->O(6*n)-->O(n) constantwill remove
# time complexity will be O(n)
