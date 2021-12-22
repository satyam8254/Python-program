'''n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
maxRow = 0
maxRowarr = []
for i in range(n):
    if arr[i] >= maxRow:
        maxRow = arr[i]
        maxRowarr.append(arr[i])
    else:
        maxRowarr.append(maxRow)
for i in range(len(maxRowarr)):
    print(maxRowarr[i])
'''









'''n = int(input())
prevNum=0
for i in range(n):
    num = int(input())
for i in range(n):
    if num[i]==0 or num[i]<0:
        print(num)
    elif num[i]>=prevNum:
        print(num[i])
    else:
        print(prevNum)'''

'''
n = int(input())
for i in range(n):
    num = int(input())
for i in range(n):
    if num[i]<num[i+1]:
        continue
    else:
        print(num[i])
'''
n=int(input())
l1=[]
for i in range(n):
    num=int(input())
    l1.append(num)
mx=l1[0]
for i in range(len(l1)):
    if l1[i]>mx:
        mx=l1[i]
    print(mx)



